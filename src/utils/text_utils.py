def split_text(text: str, max_length: int) -> list:
    paragraphs = text.split('\n\n')
    parts = []
    current_part = []

    for paragraph in paragraphs:
        if len("\n\n".join(current_part + [paragraph])) <= max_length:
            current_part.append(paragraph)
        else:
            parts.append("\n\n".join(current_part))
            current_part = [paragraph]

    if current_part:
        parts.append("\n\n".join(current_part))

    return parts