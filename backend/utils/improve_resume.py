def improve_bullets(bullets):
    improved = []
    for b in bullets:
        b_clean = b.strip()
        # Capitalize first word
        b_improved = b_clean[0].upper() + b_clean[1:]
        # Ensure it starts with an action verb (optional: add 'Developed', 'Implemented')
        if not b_improved.lower().startswith(('developed','implemented','designed')):
            b_improved = "Developed: " + b_improved
        improved.append(b_improved)
    return improved
