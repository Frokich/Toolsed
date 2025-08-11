# `listtools` — List and Iterable Utilities

Functions for working with lists, flattening, filtering, and batching.

---

### `flatten(nested_list)`

Flattens a list of lists into a single-level list. Only flattens one level deep.

**Returns:** Flat list

```python
from toolsed import flatten

flatten([[1, 2], [3], 4])  # → [1, 2, 3, 4]
flatten([1, 2, 3])         # → [1, 2, 3]
flatten([[1, 2], [3, [4]]]) # → [1, 2, 3, [4]]
```

---

### `ensure_list(obj)`

Ensures the input is a list. Wraps scalars, converts tuples, returns `[]` for `None`.

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

Removes falsy values (`None`, `False`, `0`, `""`, `[]`, `{}`) from an iterable.

**Returns:** List without falsy values

```python
from toolsed import compact

compact([0, 1, "", "a", None, [], [1], False, True])  # → [1, "a", [1], True]
```

---

### `chunks(iterable, n)`

Splits an iterable into chunks of size `n`.

Useful for batching data (e.g., API requests).

**Yields:** Lists of size `n` (last chunk may be smaller)

```python
from toolsed import chunks

list(chunks(range(7), 3))  # → [[0,1,2], [3,4,5], [6]]
```
