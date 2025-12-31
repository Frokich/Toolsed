class Functions:
    def first(self, iterable, default=None):
        return next(iter(iterable), default)

    def last(self, iterable, default=None):
        try:
            return list(iterable)[-1]
        except (IndexError, TypeError, StopIteration):
            return default

    def noop(self, *_args, **_kwargs):
        pass

    def always(self, value):
        return lambda *_args, **_kwargs: value

    def is_iterable(self, obj):
        if isinstance(obj, (str, bytes)):
            return False
        try:
            iter(obj)
            return True
        except TypeError:
            return False

    def iden(self, x):
        return x

    def tap(self, obj, func):
        func(obj)
        return obj

    def lmap(self, func, iterable):
        return (list(map(func, iterable)))

    def lfilter(self, func, iterable):
        return list(filter(func, iterable))

    def falsy(self, value):
        return not value

    def truthy(self, value):
        return bool(value)
