def moving_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        return []
    out: list[float] = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        window_vals = values[start : i + 1]
        out.append(sum(window_vals) / len(window_vals))
    return out

