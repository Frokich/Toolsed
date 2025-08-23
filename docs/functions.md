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


---

### `iden(x)`

Returns the input unchanged. Useful as a default function in `map`, `filter`, etc.

**Parameters**
- `x`: Any value

**Returns**: The same value

```python
from toolsed import identity

list(map(identity, [1, 2, 3]))  # -> [1, 2, 3] 
```

---

### tap(obj, func)

Calls `func(obj)` and returns `obj`. Useful for debugging or side effects.

**Parameters**
- `obj`: Any object
- `func`: Function to call with `obj`

**Returns**: `obj` (unchanged)

```python
from toolsed import tap

data = tap([1, 2, 3], print)  # Print the list, returns it.
```

---

### lmap(func, iterable)

Like `map()`, but returns a list directly.

**Parameters**:
- `func`: Function to apply
- `iterable`: Any iterable

**Returns**: List of results.

```python
from toolsed import lmap

lmap(str, [1, 2, 3])  # -> ['1', '2', '3']
```

---

### lfilter(func, iterable)

Like a `filter()`, but returns a list directly.

**Parameters**:
- `func`: Predicate function
- `iterable`: Any iterable

**Returns**: List of filtered items

```python
from toolsed import lfilter

lfilter(lambda x: x > 2, [1, 2, 3, 4])  # -> [3, 4]
```

---

### falsy(value)

Returns `True` if value is falsy (`None`, `()`, `""`, `[]`, `{}`, etc.).

**Parameters**:
- `value`: Any value

**Returns**: `True` if falsy,`False` otherwise

```python
from toolsed import falsy

falsy(None)         # -> True
falsy("Some text")  # -> False
```

---

### Truthy(value)

Returns `True` if value is truthy (opposite of `falsy`)

**Parameters**: 
- `value`: Any value

**Returns**: `True` if truthy, `False` otherwise

```python
from toolsed import truthy

truthy(42)  # -> True
truthy("")  # -> False
truthy([1]) # -> True
```
```
```
```
```

```
```


