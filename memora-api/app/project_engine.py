projects = {}


def create_project(name):
    if name not in projects:
        projects[name] = {
            "name": name,
            "settings": {
                "style": "",
                "lighting": "",
                "camera": "",
                "aspect_ratio": "",
                "mood": "",
            },
            "memories": {},
        }

    return projects[name]


def get_all_projects():
    return list(projects.values())


def get_project(name):
    return projects.get(name)


def get_project_settings(project_name):
    project = projects.get(project_name)

    if not project:
        return None

    return project["settings"]


def update_project_settings(
    project_name,
    style=None,
    lighting=None,
    camera=None,
    aspect_ratio=None,
    mood=None,
):
    if project_name not in projects:
        create_project(project_name)

    settings = projects[project_name]["settings"]

    if style is not None:
        settings["style"] = style

    if lighting is not None:
        settings["lighting"] = lighting

    if camera is not None:
        settings["camera"] = camera

    if aspect_ratio is not None:
        settings["aspect_ratio"] = aspect_ratio

    if mood is not None:
        settings["mood"] = mood

    return settings


def create_project_memory(
    project_name,
    memory_name,
    style,
    asset_type,
    primary_color,
    reference_image=None,
):
    if project_name not in projects:
        create_project(project_name)

    projects[project_name]["memories"][memory_name] = {
        "name": memory_name,
        "style": style,
        "asset_type": asset_type,
        "primary_color": primary_color,
        "reference_image": reference_image,
    }

    return projects[project_name]["memories"][memory_name]


def get_project_memories(project_name):
    project = projects.get(project_name)

    if not project:
        return None

    return list(project["memories"].values())


def get_project_memory(project_name, memory_name):
    project = projects.get(project_name)

    if not project:
        return None

    return project["memories"].get(memory_name)