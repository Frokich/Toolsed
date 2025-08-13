from toolsed import without

class TestWithout:
    def test_without_simple_values(self):
        assert without([1, 2, 3, 2, 1], 1) == [2, 3, 2]
        assert without([1, 2, 3, 2, 1], 1, 2) == [3]
        assert without([1, 2, 3], 4) == [1, 2, 3]  # No changes
        assert without([], 1) == []

    def test_without_multiple_types(self):
        data = [1, "hello", 2, None, "hello", 3.14, True, False]
        assert without(data, "hello", None, True) == [1, 2, 3.14, False]

    def test_without_strings_and_iterables(self):
        assert without("hello world", "l", "o") == ['h', 'e', ' ', 'w', 'r', 'd']
        assert without(("a", "b", "c"), "b") == ['a', 'c']

    def test_without_no_removals(self):
        assert without([1, 2, 3]) == [1, 2, 3]
        assert without([1, 2, 3], 4, 5,) == [1, 2, 3]

    def test_without_all_removals(self):
        assert without([1, 1, 1], 1) == []
