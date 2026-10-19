# Memora

**A full-stack AI consistency platform for maintaining characters, subjects, objects, and brand identities across AI-generated media.**

Memora provides a persistent identity and context layer for generative AI workflows, allowing creators to reuse structured identity information across multiple scenes and generations instead of rebuilding context for every prompt.

---

## The Problem

Generative AI models can create impressive individual outputs, but maintaining consistency across multiple generations is still difficult.

A character's face, hairstyle, clothing, visual style, or other defining characteristics can change between scenes even when prompts are similar.

This becomes a major problem when generating:

- Character-driven content
- Marketing campaigns
- Storyboards
- Social media creatives
- Brand assets
- Multi-scene AI content

Memora explores a product layer that sits between the user and generation providers to manage this consistency.

---

## How Memora Works

Memora organizes generation workflows around three main concepts:

### Projects

A workspace containing the identities, scenes, generation settings, and provider configuration for a piece of content.

### Profiles

Reusable identity definitions containing information about a character, subject, object, or brand.

Profiles act as persistent memory that can be injected into future generations.

### Scenes

Individual generation contexts that combine:

- User prompts
- Selected profiles
- Project settings
- Identity constraints
- Generation parameters

Before sending a request to an external AI provider, Memora builds additional context from these components and constructs an optimized generation prompt.

---

## Core Features

- Project-based generation workflows
- Reusable identity profiles
- Character and subject memory
- Scene-based generation
- Identity-aware prompt construction
- Reference locking
- Provider configuration
- Persistent project settings
- External AI provider integration
- Similarity evaluation
- Generation history and iteration
- Modular generation pipeline

---

## Architecture

Memora is built as a full-stack application with the frontend and AI generation pipeline separated through REST APIs.

```text
User
  |
  v
Next.js / React Frontend
  |
  v
REST API
  |
  v
FastAPI Backend
  |
  +----------------------+
  |                      |
  v                      v
Project / Profile      Context Engine
Management               |
                          v
                    Prompt Builder
                          |
                          v
                    AI Provider API
                          |
                          v
                   Generated Output
                          |
                          v
                 Similarity Evaluation
                          |
                          v
                     Result / UI
```

This architecture keeps provider-specific generation logic separate from the application's identity and context management.

---

## Tech Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- Python
- FastAPI
- REST APIs

### Data

- SQL-based persistence
- Project, profile, scene, provider, and settings management

### AI / Generation

- LLM-assisted workflows
- External AI generation APIs
- Context construction
- Prompt optimization
- Identity constraints
- Similarity evaluation

### Development

- Git
- GitHub
- API testing
- Debugging
- AI-assisted development

---

## Generation Pipeline

A generation request moves through multiple stages:

```text
User Prompt
    ↓
Selected Identity Profiles
    ↓
Context Construction
    ↓
Constraint Injection
    ↓
Prompt Optimization
    ↓
Provider Request
    ↓
Generated Media
    ↓
Similarity Evaluation
    ↓
Result
```

Breaking generation into separate stages also makes failures easier to debug.

Instead of treating an incorrect generation as a single model failure, Memora allows issues to be isolated across context construction, prompt generation, provider communication, generation output, and similarity evaluation.

---

## Similarity Evaluation

Memora includes an experimental similarity system for evaluating whether generated outputs preserve important characteristics from their references.

The current approach considers signals such as:

- Identity similarity
- Colour consistency
- Structural / edge similarity

Similarity evaluation is intended to support the consistency workflow rather than act as the core product itself.

---

## Product Philosophy

Memora is designed around a simple idea:

> AI models generate content. Memora remembers what should stay consistent.

The goal is not to replace generation models.

Instead, Memora acts as a consistency and identity layer that can work across generation providers.

This also allows the underlying model or provider to change without requiring the user to recreate the identity context for their project.

---

## Current Development

Memora is currently under active development.

The MVP focuses on:

- Projects
- Identity profiles
- Scenes
- Persistent project settings
- Provider connections
- Identity-aware generation
- Prompt optimization
- Similarity evaluation
- Generation workflow reliability

Development has involved debugging issues across the frontend, REST APIs, backend state, provider integrations, data persistence, and model outputs.


## Status

🚧 **Active Development**

Memora is currently an MVP and is being actively developed and iterated.

---

## Author

**Karan Kumar**

B.Tech Computer Science Engineering — AI & Data Science

GitHub: [KaranKumar0408](https://github.com/KaranKumar0408)

LinkedIn: [karankumar04](https://www.linkedin.com/in/karankumar04/)
