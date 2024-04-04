def str_is_not_empty(value: any) -> str | None:
    if value is None:
        return None
    
    value = str(value).strip()
    if value == "":
        return None
    
    return value