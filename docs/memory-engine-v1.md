# Memora Memory Engine V1

## Goal

Extract the defining characteristics of an asset and store them as a reusable memory profile.

The memory profile should be usable across:

* Regenerations
* Edits
* Different AI models
* Different versions

---

# Inputs

Supported Inputs:

* Image
* Video (future)

---

# Output

```json
{
  "asset_id": "...",
  "memory_profile": {
    "identity": {},
    "style": {},
    "composition": {},
    "color": {}
  }
}
```

---

# Memory Layers

## Layer 1: Identity Memory

Purpose:

Determine what the asset actually is.

Examples:

Character:

* Face
* Hair
* Body shape

Product:

* Shape
* Branding
* Logo

Environment:

* Buildings
* Layout
* Major objects

Stored Data:

* Embeddings
* Object labels
* Reference image

---

## Layer 2: Style Memory

Purpose:

Determine how the asset looks.

Examples:

* Realistic
* Anime
* Pixar
* Cinematic
* Watercolor

Stored Data:

* Style embedding
* Style tags

---

## Layer 3: Color Memory

Purpose:

Preserve visual identity.

Examples:

* Brand colors
* Character palette
* Scene palette

Stored Data:

* Dominant colors
* Color histogram
* Palette vectors

---

## Layer 4: Composition Memory

Purpose:

Preserve structure.

Examples:

* Camera angle
* Framing
* Subject placement

Stored Data:

* Layout metadata
* Scene structure

---

# Memory Extraction Pipeline

Asset Upload
↓
Asset Analyzer
↓
Feature Extraction
↓
Memory Builder
↓
Memory Profile Stored

---

# Asset Analyzer

Purpose:

Understand the asset.

Potential Models:

* Gemini Vision
* GPT Vision
* Florence
* Grounding DINO

Outputs:

Example:

```json
{
  "objects": [
    "person",
    "jacket"
  ],
  "scene": "urban street",
  "style": "cinematic"
}
```

---

# Feature Extraction

Purpose:

Create machine-readable fingerprints.

Examples:

Identity Embedding
Style Embedding
Color Embedding

Potential Models:

* CLIP
* DINOv2
* SigLIP

---

# Memory Builder

Combines:

* Asset analysis
* Embeddings
* Metadata

Into:

```json
{
  "identity": {},
  "style": {},
  "composition": {},
  "colors": {}
}
```

---

# Edit Workflow

User Request:

"Change jacket to blue"

↓

Load Memory Profile

↓

Generate Constraints

↓

Send To AI Model

Example:

Maintain:

* Face
* Hair
* Style
* Lighting

Change:

* Jacket Color

↓

Generate New Asset

---

# Similarity Engine

Compare:

Original Asset
vs
Generated Asset

Categories:

Identity Similarity
Style Similarity
Color Similarity
Composition Similarity

---

# Consistency Score

Example:

Identity: 99%
Style: 97%
Color: 95%
Composition: 96%

Overall: 97%

---

# V1 Success Criteria

Memora should correctly:

1. Store memory for an image.
2. Preserve selected attributes.
3. Detect major changes.
4. Generate a consistency score.
5. Track versions.

```
```


# Attribute Locking System

## Core Principle

Consistency is not determined by a universal weighting system.

Consistency is determined by what the user considers important.

Memora allows users to define which attributes must remain unchanged across generations and edits.

These are called Locked Attributes.

---

# Locked vs Editable Attributes

Every asset contains two categories:

## Locked Attributes

Must remain consistent.

Examples:

* Character face
* Hair
* Product shape
* Logo placement
* Brand colors
* Scene layout
* Art style

---

## Editable Attributes

Allowed to change.

Examples:

* Clothing
* Accessories
* Background
* Lighting
* Camera angle
* Props

---

# Asset Templates

Different asset types require different consistency priorities.

## Character Template

Default Locked Attributes:

* Face
* Hair
* Style

Default Editable Attributes:

* Clothing
* Accessories
* Pose
* Background

---

## Product Template

Default Locked Attributes:

* Product Shape
* Logo
* Branding

Default Editable Attributes:

* Background
* Camera Angle
* Environment

---

## Environment Template

Default Locked Attributes:

* Layout
* Architecture
* Atmosphere

Default Editable Attributes:

* Props
* Vehicles
* Characters
* Weather

---

## Marketing Creative Template

Default Locked Attributes:

* Product
* Logo
* Brand Colors

Default Editable Attributes:

* Background
* Promotional Elements
* Text

---

# Dynamic Weight Generation

Weights are automatically generated based on:

1. Asset Type
2. Locked Attributes
3. User Preferences

There is no global weighting model.

---

# Example: Character Asset

User Locks:

✓ Face
✓ Hair
✓ Style

User Leaves Editable:

✏ Clothing
✏ Background

Generated Weights:

Face: 40%
Hair: 25%
Style: 20%
Clothing: 5%
Background: 10%

These weights are generated dynamically.

---

# Example: Product Asset

User Locks:

✓ Product Shape
✓ Logo
✓ Brand Colors

User Leaves Editable:

✏ Background
✏ Lighting

Generated Weights:

Shape: 40%
Logo: 30%
Brand Colors: 20%
Background: 5%
Lighting: 5%

---

# Consistency Score

The Consistency Score is calculated using dynamically generated weights.

Example:

Face Similarity: 99%
Hair Similarity: 97%
Style Similarity: 95%
Background Similarity: 70%

Overall Consistency: 96%

The score prioritizes locked attributes and minimizes the influence of editable attributes.

---

# Future Vision

Eventually Memora should automatically suggest:

* What should be locked
* What can be edited
* Which attributes are most important

using AI-powered asset analysis.

Users can then accept, reject, or customize these recommendations.
