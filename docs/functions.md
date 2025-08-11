# `functions` — General-Purpose Utilities

Core utility functions for everyday Python programming.

---

### `first(iterable, default=None)`

Returns the first item from an iterable, or `default` if empty.

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

Returns the last item from an iterable, or `default` if empty or not iterable.

**Parameters:**
- `iterable`: Any iterable
- `default`: Value to return if empty

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

Useful as a default callback.

```python
from toolsed import noop

on_complete = noop
on_complete("Done!")  # → no effect
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

Checks if an object is iterable, excluding strings and bytes.

**Returns:** `True` if iterable and not a string/bytes

```python
from toolsed import is_iterable

is_iterable([1, 2])     # → True
is_iterable("hello")    # → False
is_iterable((1, 2))     # → True
is_iterable(42)         # → False
```
