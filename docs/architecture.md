# Memora Architecture v1

## Overview

Memora is a memory and consistency layer that sits between creators and generative AI models.

Instead of users interacting directly with image and video generation models, they interact with Memora.

Memora handles:

* Asset memory
* Version control
* Consistency enforcement
* AI orchestration
* Asset storage

AI models become interchangeable engines.

Memory becomes the product.

---

# High-Level System Architecture

```text
User
  ↓
Frontend (Next.js)
  ↓
Backend API (FastAPI)
  ↓
Memory Engine
  ↓
AI Provider Layer
  ↓
Storage & Database
```

---

# Frontend Layer

## Technology

* Next.js
* TypeScript
* Tailwind CSS

## Responsibilities

### Dashboard

Displays:

* Projects
* Recent assets
* Activity

### Project Page

Displays:

* Asset library
* Upload actions
* Generation actions

### Asset Page

Displays:

* Asset preview
* Memory profile
* Consistency score
* Edit controls

### Versions Page

Displays:

* Version history
* Change tracking
* Consistency comparisons

---

# Backend Layer

## Technology

* FastAPI
* Python

## Responsibilities

### Authentication

Future:

* Google Login
* Studio Accounts
* Team Management

---

### Asset Management

Create:

* Projects
* Assets
* Versions

Store:

* Metadata
* Memory profiles
* Version history

---

### AI Orchestration

Responsible for:

* Model selection
* Prompt construction
* Consistency constraints
* Generation requests

The frontend never directly talks to AI providers.

---

# Memory Engine

## Purpose

The Memory Engine is the core intellectual property of Memora.

It determines:

* What defines an asset
* What must remain consistent
* What is allowed to change

---

## Responsibilities

### Memory Extraction

Input:

```text
Image / Video
```

Output:

```json
{
  "identity": {},
  "style": {},
  "composition": {},
  "colors": {}
}
```

---

### Memory Storage

Stores:

* Embeddings
* Tags
* Reference assets
* Locked attributes

---

### Similarity Analysis

Compares:

```text
Original Asset
vs
Generated Asset
```

Produces:

```text
Identity Similarity
Style Similarity
Color Similarity
Overall Consistency Score
```

---

# AI Provider Layer

## Purpose

Provide a unified interface for multiple AI models.

Users should not care which model is used.

---

## Initial Providers

### OpenAI

Use for:

* Image generation
* Image editing

---

### Google Gemini

Use for:

* Image understanding
* Metadata extraction

---

### Flux

Use for:

* High-quality image generation

---

## Future Providers

* Runway
* Kling
* Pika
* Luma
* Veo
* Midjourney (if APIs become available)

---

# Database Layer

## Technology

PostgreSQL

---

## Core Tables

### Projects

```sql
id
name
created_at
updated_at
```

---

### Assets

```sql
id
project_id
name
type
current_version_id
```

---

### Versions

```sql
id
asset_id
version_number
prompt
consistency_score
created_at
```

---

### Memory Profiles

```sql
id
asset_id
memory_data
created_at
```

---

# Storage Layer

## Purpose

Store:

* Images
* Videos
* Thumbnails

---

## Initial Options

### Cloudinary

Advantages:

* Easy setup
* CDN included
* Media transformations

---

### AWS S3

Advantages:

* Scalable
* Industry standard

---

# Generation Workflow

## Create Asset

User Request
↓
Backend
↓
AI Provider
↓
Generated Asset
↓
Memory Extraction
↓
Store Asset
↓
Store Memory Profile

---

# Edit Asset Workflow

User Edit Request
↓
Load Memory Profile
↓
Generate Consistency Constraints
↓
AI Provider
↓
Receive Updated Asset
↓
Similarity Analysis
↓
Calculate Consistency Score
↓
Create New Version

---

# Consistency Scoring

Future categories:

### Identity

Examples:

* Character face
* Product shape

---

### Style

Examples:

* Art style
* Rendering style

---

### Composition

Examples:

* Camera angle
* Framing

---

### Color

Examples:

* Color palette
* Brand colors

---

### Motion (Video)

Examples:

* Camera movement
* Subject movement

---

# V1 Scope

Must Have:

* Projects
* Assets
* Versions
* Image Generation
* Memory Profiles
* Consistency Scores

---

# V2 Scope

* Video Support
* Team Collaboration
* Shared Libraries
* Advanced Memory Rules
* Multi-Asset Consistency

---

# Long-Term Vision

Memora becomes the operating system for generative media production.

Studios, agencies, and creators manage all AI-generated assets through Memora rather than interacting directly with individual AI models.

The memory layer becomes the source of truth for every generated asset.
