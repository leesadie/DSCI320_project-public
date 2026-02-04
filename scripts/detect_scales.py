def detect_scales(df, fields, overrides=None):
    """
    Detect and apply scales for skewed variables
    """
    overrides = overrides or {}
    scales = {}

    for field in fields:
        series = df[field].dropna()
        nonzero = series[series > 0]
        if len(nonzero) < 2:
            scales[field] = 'linear'
            continue 

        ratio = nonzero.max() / nonzero.min()

        if ratio > 1e6:
            scales[field] = 'log'
        elif ratio > 100:
            scales[field] = 'sqrt'
        else:
            scales[field] = 'linear' # Default to linear

    # Manual overrides
    for k, v in overrides.items():
        if k in fields:
            scales[k] = v

    return scales