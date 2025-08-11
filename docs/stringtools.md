# `stringtools` — String Utilities

Functions for string manipulation and formatting.

---

### `truncate(text, length, suffix="...")`

Truncates a string to a given length, appending a suffix if needed.

If the suffix is longer than `length`, returns the first `length` characters of the text.

**Returns:** Truncated string

```python
from toolsed import truncate

truncate("Hello world", 8)     # → "Hello..."
truncate("Short", 10)          # → "Short"
truncate("Hi", 1)              # → "H"
truncate("Test", 4, "..")      # → "Te.."
```

---

### `pluralize(count, singular, plural=None)`

Returns a string like `"1 file"`, `"2 files"`, etc.

If `plural` is not provided, adds `"s"` to `singular`.

**Returns:** Formatted string with correct pluralization

```python
from toolsed import pluralize

pluralize(1, "file")           # → "1 file"
pluralize(2, "file")           # → "2 files"
pluralize(5, "яблоко", "яблок") # → "5 яблок"
pluralize(1, "item")           # → "1 item"
```
