def safe_get(d, *keys, default=None):
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return default

    if isinstance(d, dict):
        return default
    return d


def dict_merge(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


def deep_merge(*dicts):
    result = {}
    for d in dicts:
        if not isinstance(d, dict):
            continue
        for k, v in d.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = deep_merge(result[k], v)
            else:
                result[k] = v
    return result


def pick(d, *keys):
    return {k: d[k] for k in keys if k in d}


def omit(d, *keys):
    return {k: v for k, v in d.items() if k not in keys}



