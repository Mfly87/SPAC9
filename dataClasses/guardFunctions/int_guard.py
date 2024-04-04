def int_is_int(value: any) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            value = int(value)
            return value
        except:
            return None
    return None
    
def int_is_one_or_greater(value: any) -> int | None:
    value = int_is_int(value)
    if value is None:
        return None
    if 1 <= value:
        return value
    return None