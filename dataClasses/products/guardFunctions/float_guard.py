def float_is_float(value: any) -> float | None:
    if value is None:
        return None
    if isinstance(value, int):
        return float(value)
    if isinstance(value, float):
        return value
    if isinstance(value, str):
        try:
            value = value.replace(".","")
            value = float(value)
            return value
        except:
            return None
    return None
    
def float_is_zero_or_greater(value: any) -> float | None:
    value = float_is_float(value)
    if value is None:
        return None
    if 0.0 <= value:
        return value
    return None
    
def float_is_between_one_and_one_hundred(value: any) -> float | None:
    value = float_is_float(value)
    if value is None:
        return None
    if 0.0 <= value and value <= 100.0:
        return value
    return None