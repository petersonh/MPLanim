def lerp(a: int, b: int, t: float) -> int:
    return int((a * (1.0 - t)) + (b * t))

def lerp_float(a: float, b: float, t: float) -> float:
    return (a * (1.0 - t)) + (b * t)