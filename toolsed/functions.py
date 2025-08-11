def first(iterable, default=None):
    return next(iter(iterable), default)


def last(iterable, default=None):
    try:
        return list(iterable)[-1]
    except (IndexError, TypeError, StopIteration):
        return default


def noop(*_args, **_kwargs):
    pass

def always(value):
    return lambda *_args, **_kwargs: value

def is_iterable(obj):
    if isinstance(obj, (str, bytes)):
        return False
    try:
        iter(obj)
        return True
    except TypeError:
        return False

