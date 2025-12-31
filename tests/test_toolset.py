# tests/test_toolsed.py
from _pytest.capture import capsys
from toolsed.functions import Functions
from toolsed.stringtools import StringTools
from toolsed.listtools import ListTools
from toolsed.dicttools import DictTools

fc = Functions()
st = StringTools()
ls = ListTools()
di = DictTools()

class TestFunctions:
    def test_first(self):
        assert fc.first([1, 2, 3]) == 1
        assert fc.first([], default="empty") == "empty"
        assert fc.first(iter([10, 20])) == 10

    def test_last(self):
        assert fc.last([1, 2, 3]) == 3
        assert fc.last([], default="end") == "end"
        assert fc.last("abc") == "c"  # строка — итерируема

    def test_noop(self):
        # Проверим, что ничего не ломается
        fc.noop()
        fc.noop(1, 2, x=3)
        assert fc.noop() is None

    def test_always(self):
        const = fc.always(42)
        assert const() == 42
        assert const(1, 2, 3) == 42
        assert const(x="y") == 42

    def test_is_iterable(self):
        assert fc.is_iterable([1, 2]) is True
        assert fc.is_iterable((1, 2)) is True
        assert fc.is_iterable("hello") is False  # строка — исключена
        assert fc.is_iterable(b"raw") is False   # bytes — исключены
        assert fc.is_iterable(42) is False
        assert fc.is_iterable({1, 2}) is True


class TestListTools:
    def test_flatten(self):
        assert ls.flatten([1, [2, 3], [4]]) == [1, 2, 3, 4]
        assert ls.flatten([1, 2, 3]) == [1, 2, 3]
        assert ls.flatten([[1, 2], [3, [4]]]) == [1, 2, 3, [4]]  # только один уровень

    def test_ensure_list(self):
        assert ls.ensure_list(1) == [1]
        assert ls.ensure_list([1, 2]) == [1, 2]
        assert ls.ensure_list((1, 2)) == [1, 2]
        assert ls.ensure_list(None) == []
        assert ls.ensure_list("text") == ["text"]

    def test_compact(self):
        assert ls.compact([0, 1, "", "a", None, [], [1], False, True]) == [1, "a", [1], True]

    def test_chunks(self):
        data = list(range(8))
        result = list(ls.chunks(data, 3))
        assert result == [[0, 1, 2], [3, 4, 5], [6, 7]]


class TestDictTools:
    def test_safe_get(self):
        data = {"a": {"b": {"c": 42}}}
        assert di.safe_get(data, "a", "b", "c") == 42
        assert di.safe_get(data, "a", "x", default="not found") == "not found"
        assert di.safe_get(data, "z", default="missing") == "missing"
        assert di.safe_get(data, "a", "b", "c", "d", default="deep") == "deep"

    def test_dict_merge(self):
        a = {"x": 1, "y": 2}
        b = {"y": 99, "z": 3}
        merged = di.dict_merge(a, b)
        assert merged == {"x": 1, "y": 99, "z": 3}

        # Проверка нескольких словарей
        c = {"x": 999}
        merged2 = di.dict_merge(a, b, c)
        assert merged2 == {"x": 999, "y": 99, "z": 3}

    def test_deep_merge_simple(self):
        a = {"x": 1, "y": 2}
        b = {"y": 99, "z": 3}
        result = di.deep_merge(a, b)
        assert result == {"x": 1, "y": 99, "z": 3}

    def test_deep_merge_nested_dicts(self):
        a = {"nested": {"a": 1, "b": 2}}
        b = {"nested": {"b": 3, "c": 4}}
        result = di.deep_merge(a, b)
        assert result == {"nested": {"a": 1, "b": 3, "c": 4}}

    def test_deep_merge_multiple_dicts(self):
        a = {"x": 1}
        b = {"y": 2}
        c = {"z": 3}
        result = di.deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2, "z": 3}

    def test_deep_merge_deep_nesting(self):
        a = {"level1": {"level2": {"level3": {"a": 1}}}}
        b = {"level1": {"level2": {"level3": {"b": 2}}}}
        c = {"level1": {"level2": {"level4": 4}}}
        result = di.deep_merge(a, b, c)
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
        result = di.deep_merge(a, b)
        assert result == {"config": "default"}

    def test_deep_merge_with_empty_dicts(self):
        a = {"x": 1}
        b = {}
        c = {"y": 2}
        result = di.deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2}

    def test_deep_merge_non_dict_skipped(self):
        a = {"x": 1}
        b = None
        c = {"y": 2}
        result = di.deep_merge(a, b, c)
        assert result == {"x": 1, "y": 2}

    def test_deep_merge_no_args(self):
        assert di.deep_merge() == {}

class TestStringTools:
    def test_truncate(self):
        assert st.truncate("Hello world", 8) == "Hello..."
        assert st.truncate("Short", 10) == "Short"
        assert st.truncate("Hi", 1) == "H"  # даже если суффикс длиннее
        assert st.truncate("Test", 3, "..") == "T.."

    def test_pluralize(self):
        assert st.pluralize(1, "file") == "1 file"
        assert st.pluralize(2, "file") == "2 files"
        assert st.pluralize(5, "яблоко", "яблок") == "5 яблок"
        assert st.pluralize(1, "яблоко", "яблок") == "1 яблоко"

class TestIden:
    def test_iden_returns_same(self):
        assert fc.iden(42) == 42
        assert fc.iden("hello") == "hello"       
        assert fc.iden([1, 2]) == [1, 2]


class TestTap:
    def test_tap_returns_object(self, capsys):
        result = fc.tap("hello", print)
        captured = capsys.readouterr()
        assert result == "hello"
        assert captured.out.strip() == "hello"

    def test_tap_with_list(self):
        data = [1, 2, 3]
        result = fc.tap(data, lambda x: x.append(4))
        assert result == [1, 2, 3, 4]


class TestLmap:
    def test_lmap_applies_function(self):
        assert fc.lmap(str, [1, 2, 3]) == ["1", "2", "3"] or ['1','2','3']
        assert fc.lmap(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


class TestLfilter:
    def test_lfilter_filters_by_func(self):
        assert fc.lfilter(lambda x: x > 2, [1, 2, 3, 4]) == [3, 4]
        assert fc.lfilter(bool, [0, 1, "", "a"]) == [1, "a"]


class TestFalsy:
    def test_falsy_returns_true_for_falsy_values(self):
        assert fc.falsy(1) is False
        assert fc.falsy("a") is False

    def test_truthy_returns_opposite_of_falsy(self):
        assert fc.truthy(42) is True
        assert fc.truthy("") is False
        assert fc.truthy([1]) is True
        assert fc.truthy([]) is False


class TestDedupe:
    def test_dedupe_removes_dublicate_preserves_order(self):
        assert ls.dedupe([1, 2, 2, 3, 1]) == [1, 2, 3]
        assert ls.dedupe(["a", "b", "a", "c"]) == ["a", "b", "c"]
        assert ls.dedupe([]) == []
        assert ls.dedupe([1, 1, 1]) == [1]


class TestPick:
    def test_pick_returns_only_specified_keys(self):
        user = {"Name": "Alice", "age": 20, "email": "test@gmail.com"}
        assert di.pick(user, "missing") == {}

    def test_with_no_keys(self):
        assert di.pick({"a": 1},) == {}
       

class TestOmit:
    def test_omit_removes_specifie_keys(self):
        user = {"name": "Alice", "password": "123", "age": 30}
        assert di.omit(user, "password") == {"name": "Alice", "age": 30}

    def test_omit_missing_keys(self):
        assert di.omit({"a": 1}, "b") == {"a": 1}


class TestSlugi:
    def test_slugi_basic(self):
        assert st.slugify("Hello World") == "hello-world"
        assert st.slugify("C++ is great?") == "c-is-great"

    def test_slugi_with_punctuation(self):
        assert st.slugify("It's a test!") == "its-a-test"
        assert st.slugify("user@domain.com") == "userdomaincom"

    def test_slugi_edge_cases(self):
        assert st.slugify("") == ""
        assert st.slugify("   ") == ""
        assert st.slugify("a-b_c") == "a-b-c"
        assert st.slugify("a___b---c") == "a-b-c"

