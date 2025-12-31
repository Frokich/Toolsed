import itertools

class ListTools:
    def flatten(self, nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(item)
            else:
                result.append(item)
        return result


    def ensure_list(self, obj):
        if obj is None:
            return []
        if isinstance(obj, (list, tuple)):
            return list(obj)
        return [obj]


    def compact(self, iterable):
        return [x for x in iterable if x]


    def chunks(self, iterable, n):
        it = iter(iterable)
        while True:
            chunk = list(itertools.islice(it, n))
            if not chunk:
                break
            yield chunk


    def without(self, iterable, *values):
        if isinstance(iterable, str):
            result = iterable
            for value in values:
                result = result.replace(str(value), "")
            return list(result)
        else:
            return [item for item in iterable if item not in values]


    def dedupe(self, iterable):
        seen = set()
        result = []
        for item in iterable:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
