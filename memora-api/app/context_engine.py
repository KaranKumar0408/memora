def build_context(prompt, subjects):
    prompt_lower = prompt.lower()

    matched = []

    for subject in subjects:
        subject_name = subject["name"].lower()

        if subject_name in prompt_lower:
            matched.append({
                "subject": subject,
                "reason": "Mentioned directly in prompt.",
                "confidence": 1.0
            })

    return {
        "matched_subjects": matched
    }