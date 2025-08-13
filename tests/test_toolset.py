# tests/test_toolsed.py
import pytest
from toolsed import (
    first, last, noop, always, is_iterable,
    flatten, ensure_list, compact, chunks, without,
    safe_get, dict_merge, deep_merge,
    truncate, pluralize
)


class TestFunctions:
    def test_first(self):
        assert first([1, 2, 3]) == 1
        assert first([], default="empty") == "empty"
        assert first(iter([10, 20])) == 10

    def test_last(self):
        assert last([1, 2, 3]) == 3
        assert last([], default="end") == "end"
        assert last("abc") == "c"  # строка — итерируема

    def test_noop(self):
        # Проверим, что ничего не ломается
        noop()
        noop(1, 2, x=3)
        assert noop() is None

    def test_always(self):
        const = always(42)
        assert const() == 42
        assert const(1, 2, 3) == 42
        assert const(x="y") == 42

    def test_is_iterable(self):
        assert is_iterable([1, 2]) is True
        assert is_iterable((1, 2)) is True
        assert is_iterable("hello") is False  # строка — исключена
        assert is_iterable(b"raw") is False   # bytes — исключены
        assert is_iterable(42) is False
        assert is_iterable({1, 2}) is True


class TestListTools:
    def test_flatten(self):
        assert flatten([1, [2, 3], [4]]) == [1, 2, 3, 4]
        assert flatten([1, 2, 3]) == [1, 2, 3]
        assert flatten([[1, 2], [3, [4]]]) == [1, 2, 3, [4]]  # только один уровень

    def test_ensure_list(self):
        assert ensure_list(1) == [1]
        assert ensure_list([1, 2]) == [1, 2]
        assert ensure_list((1, 2)) == [1, 2]
        assert ensure_list(None) == []
        assert ensure_list("text") == ["text"]

    def test_compact(self):
        assert compact([0, 1, "", "a", None, [], [1], False, True]) == [1, "a", [1], True]

    def test_chunks(self):
        data = list(range(8))
        result = list(chunks(data, 3))
        assert result == [[0, 1, 2], [3, 4, 5], [6, 7]]


class TestDictTools:
    def test_safe_get(self):
        data = {"a": {"b": {"c": 42}}}
        assert safe_get(data, "a", "b", "c") == 42
        assert safe_get(data, "a", "x", default="not found") == "not found"
        assert safe_get(data, "z", default="missing") == "missing"
        assert safe_get(data, "a", "b", "c", "d", default="deep") == "deep"

    def test_dict_merge(self):
        a = {"x": 1, "y": 2}
        b = {"y": 99, "z": 3}
        merged = dict_merge(a, b)
        assert merged == {"x": 1, "y": 99, "z": 3}

        # Проверка нескольких словарей
        c = {"x": 999}
        merged2 = dict_merge(a, b, c)
        assert merged2 == {"x": 999, "y": 99, "z": 3}

    def test_deep_merge_simple(self):
        a = {"x": 1, "y": 2}
        b = {"y": 99, "z": 3}
        result = deep_merge(a, b)
        assert result == {"x": 1, "y": 99, "z": 3}

    def test_deep_merge_nested_dicts(self):
        a = {"nested": {"a": 1, "b": 2}}
        b = {"nested": {"b": 3, "c": 4}}
        result = deep_merge(a, b)
        assert result == {"nested": {"a": 1, "b": 3, "c": 4}}

    def test_deep_merge_multiple_dicts(self):
        a = {"x": 1}
        b = {"y": 2}
        c = {"z": 3}
        result = deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2, "z": 3}

    def test_deep_merge_deep_nesting(self):
        a = {"level1": {"level2": {"level3": {"a": 1}}}}
        b = {"level1": {"level2": {"level3": {"b": 2}}}}
        c = {"level1": {"level2": {"level4": 4}}}
        result = deep_merge(a, b, c)
        assert result == {
            "level1": {
                "level2": {
                    "level3": {"a": 1, "b": 2},
                    "level4": 4
                }
            }
        }

    def test_deep_merge_overwrite_non_dict(self):
        a = {"config": {"theme": "dark", "size": 10}}
        b = {"config": "default"}  # not a dict — should replace
        result = deep_merge(a, b)
        assert result == {"config": "default"}

    def test_deep_merge_with_empty_dicts(self):
        a = {"x": 1}
        b = {}
        c = {"y": 2}
        result = deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2}

    def test_deep_merge_non_dict_skipped(self):
        a = {"x": 1}
        b = None
        c = {"y": 2}
        result = deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2}

    def test_deep_merge_no_args(self):
        assert deep_merge() == {}

class TestStringTools:
    def test_truncate(self):
        assert truncate("Hello world", 8) == "Hello..."
        assert truncate("Short", 10) == "Short"
        assert truncate("Hi", 1) == "H"  # даже если суффикс длиннее
        assert truncate("Test", 3, "..") == "T.."

    def test_pluralize(self):
        assert pluralize(1, "file") == "1 file"
        assert pluralize(2, "file") == "2 files"
        assert pluralize(5, "яблоко", "яблок") == "5 яблок"
        assert pluralize(1, "яблоко", "яблок") == "1 яблоко"

 
# Дополнительный тест: проверка, что всё экспортируется через __all__
def test_all_exports():
    import toolsed
    exported = toolsed.__all__
    assert 'first' in exported
    assert 'safe_get' in exported
    assert 'pluralize' in exported
    assert 'is_iterable' in exported
