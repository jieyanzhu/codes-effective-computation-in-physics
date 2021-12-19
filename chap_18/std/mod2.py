def std(vals):
    n = len(vals)
    if n == 0:
        return 0.0
    mu = sum(vals) / n
    var = 0.0
    for val in vals:
        var += (val - mu)**2
    return (var / n)**0.5

