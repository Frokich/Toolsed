def truncate(text: str, length: int, suffix: str = "...") -> str:
    if len(text) <= length:
        return text

    if len(suffix) >= length:
        return text[:length]
    
    cut_len = length - len(suffix)
    return text[:cut_len] + suffix


def pluralize(count, singular, plural=None):
    if plural is None:
        plural = singular + 's'
    word = singular if count == 1 else plural
    return f"{count} {word}"


