from app.prompt_builder import compose_prompt
from app.context_engine import build_context
from app.similarity import calculate_similarity
from app.analyzer import extract_dominant_color
from app.generation_engine import generate_image

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.project_engine import (
    create_project,
    get_all_projects,
    get_project,
    create_project_memory,
    get_project_memories,
    get_project_memory,
    get_project_settings,
    update_project_settings,
)

from pydantic import BaseModel

import os
import shutil
import tempfile

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


class ProjectRequest(BaseModel):
    name: str


class MemoryRequest(BaseModel):
    name: str
    style: str
    asset_type: str
    primary_color: str


class GenerateRequest(BaseModel):
    prompt: str


class ProjectSettingsRequest(BaseModel):
    style: str = ""
    lighting: str = ""
    camera: str = ""
    aspect_ratio: str = ""
    mood: str = ""


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Memora API Running"}


@app.post("/project/create")
def create_new_project(request: ProjectRequest):
    return create_project(request.name)


@app.get("/project")
def get_projects():
    return get_all_projects()


@app.get("/project/{project_name}")
def get_single_project(project_name: str):
    project = get_project(project_name)

    if project is None:
        return {"error": "Project not found"}

    return project


@app.get("/project/{project_name}/settings")
def get_settings(project_name: str):
    settings = get_project_settings(project_name)

    if settings is None:
        return {"error": "Project not found"}

    return settings


@app.post("/project/{project_name}/settings")
def update_settings(
    project_name: str,
    request: ProjectSettingsRequest
):
    return update_project_settings(
        project_name,
        request.style,
        request.lighting,
        request.camera,
        request.aspect_ratio,
        request.mood,
    )


@app.post("/project/{project_name}/memory/create")
def create_memory_inside_project(
    project_name: str,
    request: MemoryRequest
):
    return create_project_memory(
        project_name,
        request.name,
        request.style,
        request.asset_type,
        request.primary_color,
    )


@app.post("/project/{project_name}/memory/create-from-image")
async def create_memory_from_image(
    project_name: str,
    name: str = Form(...),
    memory_type: str = Form("Character"),
    image: UploadFile = File(...)
):
    file_path = os.path.join(UPLOAD_DIR, image.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    color_data = extract_dominant_color(file_path)

    image_url = f"http://127.0.0.1:8000/uploads/{image.filename}"

    memory = create_project_memory(
        project_name,
        name,
        "Auto-detected",
        memory_type,
        color_data["label"],
        image_url,
    )

    return {
        **memory,
        "analysis": {
            "dominant_color": color_data
        }
    }


@app.get("/project/{project_name}/memories")
def get_memories_inside_project(project_name: str):
    memories = get_project_memories(project_name)

    if memories is None:
        return {"error": "Project not found"}

    return memories


@app.get("/project/{project_name}/memory/{memory_name}")
def get_single_memory_inside_project(
    project_name: str,
    memory_name: str
):
    memory = get_project_memory(project_name, memory_name)

    if memory is None:
        return {"error": "Memory not found"}

    return memory


@app.post("/project/{project_name}/generate")
def generate_with_context(
    project_name: str,
    request: GenerateRequest
):
    subjects = get_project_memories(project_name)

    if subjects is None:
        return {"error": "Project not found"}

    project_settings = get_project_settings(project_name)

    context = build_context(
        request.prompt,
        subjects
    )

    optimized_prompt = compose_prompt(
        request.prompt,
        project_settings,
        context["matched_subjects"]
    )

    generation = generate_image(
        optimized_prompt
    )

    return {
        "prompt": request.prompt,
        "optimized_prompt": optimized_prompt,
        "project_settings": project_settings,
        "context": context,
        "generation": generation,
        "status": "Context built successfully"
    }


@app.post("/compare")
async def compare_images(
    image_a: UploadFile = File(...),
    image_b: UploadFile = File(...)
):
    with tempfile.NamedTemporaryFile(delete=False) as file_a:
        file_a.write(await image_a.read())

    with tempfile.NamedTemporaryFile(delete=False) as file_b:
        file_b.write(await image_b.read())

    scores = calculate_similarity(file_a.name, file_b.name)

    return {
        **scores,
        "image_a": image_a.filename,
        "image_b": image_b.filename,
    }