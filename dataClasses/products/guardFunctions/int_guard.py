def int_is_int(value: any) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            value = value.replace(".","")
            value = int(value)
            return value
        except:
            return None
    return None
    
def int_is_X_or_greater(value: any, min_value:int) -> int | None:
    value = int_is_int(value)
    if value is None:
        return None
    if min_value <= value:
        return value
    return None


def int_is_zero_or_greater(value: any) -> int | None:
    return int_is_X_or_greater(value, 0)

def int_is_one_or_greater(value: any) -> int | None:
    return int_is_X_or_greater(value, 1)