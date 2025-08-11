# `toolsed` — Simple, Practical Utilities for Python

**`toolsed`** is a lightweight Python library that provides simple, reusable, and practical utility functions for everyday programming tasks. It’s designed to reduce boilerplate code and make common operations more readable and expressive.

No magic. No bloat. Just useful tools you'd write yourself — but already tested, documented, and ready to use.

---

## 🚀 Why `toolsed`?

In Python, you often write the same small helpers over and over:
- Get the first item from a list (or return `None` if empty)
- Safely access nested dictionaries
- Flatten a list of lists
- Truncate long strings
- Handle optional values gracefully

`toolsed` collects these patterns into one clean, reliable package so you don’t have to reinvent the wheel.

---

## 📦 Installation

Install from PyPI:

```bash
pip install toolsed
```

Or install locally in development mode:

```bash
pip install -e .
```

---

## 🧰 Functions

Below is a full list of utilities provided by `toolsed`.

---

### `first(iterable, default=None)`

Returns the first item from an iterable, or a default value if the iterable is empty.

Useful for safely getting values from lists, generators, or database queries.

**Parameters:**
- `iterable`: Any iterable (list, tuple, generator, etc.)
- `default`: Value to return if iterable is empty

**Returns:** First item or `default`

```python
from toolsed import first

first([1, 2, 3])           # → 1
first([])                  # → None
first([], default="empty") # → "empty"
first(iter(range(10)))     # → 0
```

---

### `last(iterable, default=None)`

Returns the last item from an iterable, or a default value if empty.

**Parameters:**
- `iterable`: Any iterable
- `default`: Value to return if empty or not iterable

**Returns:** Last item or `default`

```python
from toolsed import last

last([1, 2, 3])            # → 3
last("hello")              # → 'o'
last([], default="end")    # → "end"
last(None, default="n/a")  # → "n/a"
```

---

### `noop(*args, **kwargs)`

A no-operation function. Does nothing and returns `None`.

Useful as a default callback or placeholder.

```python
from toolsed import noop

on_success = noop
on_success("Done!")  # → no effect
```

---

### `always(value)`

Returns a function that always returns the given value, regardless of arguments.

**Parameters:**
- `value`: The value to always return

**Returns:** A callable that returns `value`

```python
from toolsed import always

get_default = always("unknown")
get_default()           # → "unknown"
get_default(1, 2, x=3)  # → "unknown"
```

---

### `is_iterable(obj)`

Checks if an object is iterable, but **excludes strings and bytes** (which are iterable but often treated as scalars).

**Returns:** `True` if iterable and not a string/bytes

```python
from toolsed import is_iterable

is_iterable([1, 2])     # → True
is_iterable("hello")    # → False
is_iterable((1, 2))     # → True
is_iterable(42)         # → False
```

---

### `flatten(nested_list)`

Flattens a list of lists into a single-level list. Only flattens one level deep.

**Returns:** Flat list

```python
from toolsed import flatten

flatten([[1, 2], [3], 4])  # → [1, 2, 3, 4]
flatten([1, 2, 3])         # → [1, 2, 3]
flatten([[1, 2], [3, [4]]]) # → [1, 2, 3, [4]] (only one level)
```

---

### `ensure_list(obj)`

Ensures the input is a list. Wraps scalars in a list, converts tuples, returns `[]` for `None`.

**Returns:** A list

```python
from toolsed import ensure_list

ensure_list(1)        # → [1]
ensure_list([1, 2])   # → [1, 2]
ensure_list(None)     # → []
ensure_list("text")   # → ["text"]
```

---

### `compact(iterable)`

Removes "falsy" values (`None`, `False`, `0`, `""`, `[]`, `{}`) from an iterable.

**Returns:** List without falsy values

```python
from toolsed import compact

compact([0, 1, "", "a", None, [], [1], False, True])  # → [1, "a", [1], True]
```

---

### `chunks(iterable, n)`

Splits an iterable into chunks of size `n`.

Useful for batching data (e.g., API calls).

**Yields:** Lists of size `n` (last chunk may be smaller)

```python
from toolsed import chunks

list(chunks(range(7), 3))  # → [[0,1,2], [3,4,5], [6]]
```

---

### `safe_get(d, *keys, default=None)`

Safely retrieves a value from a nested dictionary. Returns `default` if any key is missing.

**Parameters:**
- `d`: Dictionary (or any object)
- `*keys`: Chain of keys
- `default`: Value to return on failure

**Returns:** Value or `default`

```python
from toolsed import safe_get

data = {"user": {"profile": {"name": "Alice"}}}
safe_get(data, "user", "profile", "name")           # → "Alice"
safe_get(data, "user", "email", default="no@ex.com") # → "no@ex.com"
safe_get(data, "admin", "level", default=0)         # → 0
```

---

### `dict_merge(*dicts)`

Merges multiple dictionaries. Later dicts override earlier ones.

**Returns:** New merged dict

```python
from toolsed import dict_merge

a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
merged = dict_merge(a, b)  # → {"x": 1, "y": 99, "z": 3}
```

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
```

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

All functions are tested and safe for production use.

---

## 🛠️ Development

To contribute or extend:

1. Fork the repo
2. Install in dev mode: `pip install -e .`
3. Add tests in `tests/`
4. Submit a PR

---

## 📄 License

MIT License. See `LICENSE` for details.

---

> `toolsed` — because you shouldn't have to write the same helpers twice.
