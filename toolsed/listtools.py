import itertools


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def ensure_list(obj):
    if obj is None:
        return []
    if isinstance(obj, (list, tuple)):
        return list(obj)
    return [obj]


def compact(iterable):
    return [x for x in iterable if x]


def chunks(iterable, n):
    it = iter(iterable)
    while chunk := list(itertools.islice(it, n)):
        yield chunk


def without(iterable, *values):
    if isinstance(iterable, str):
        result = iterable
        for value in values:
            result = result.replace(str(value), "")
        return list(result)
    else:
        return [item for item in iterable if item not in values]
