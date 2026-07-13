def compose_prompt(user_prompt, project_settings, matched_subjects):
    settings_context = ""

    if project_settings:
        settings_context = f"""
Project Creative Settings:
Style: {project_settings.get("style", "")}
Lighting: {project_settings.get("lighting", "")}
Camera: {project_settings.get("camera", "")}
Aspect Ratio: {project_settings.get("aspect_ratio", "")}
Mood: {project_settings.get("mood", "")}

Maintain consistency with these project-level creative rules.
"""

    subject_context = []

    for match in matched_subjects:
        subject = match["subject"]

        subject_context.append(
            f"""
Subject: {subject['name']}
Type: {subject['asset_type']}
Primary Color: {subject['primary_color']}
Reason Selected: {match['reason']}
Confidence: {int(match['confidence'] * 100)}%
Keep this subject visually consistent.
"""
        )

    return f"""
You are generating an image for an existing creative project.

{settings_context}

Maintain consistency with these saved subjects:

{''.join(subject_context)}

User Request:

{user_prompt}
"""