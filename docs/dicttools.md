# `dicttools` — Dictionary Utilities

Functions from `toolsed.dicttools` for safe and convenient dictionary operations.

---

### `safe_get(d, *keys, default=None)`

Safely retrieves a value from a nested dictionary. Returns `default` if any key is missing or the value is not a dictionary.

**Parameters:**
- `d`: Dictionary or any object
- `*keys`: Chain of keys (e.g., `"user", "profile", "name"`)
- `default`: Value to return if path doesn't exist

**Returns:** The value at the key path, or `default`

```python
from toolsed import safe_get

data = {"user": {"profile": {"name": "Alice"}}}
safe_get(data, "user", "profile", "name")           # → "Alice"
safe_get(data, "user", "email", default="no@ex.com") # → "no@ex.com"
safe_get(data, "admin", "level", default=0)         # → 0
safe_get(None, "a", "b", default="missing")         # → "missing"
```

---

### `dict_merge(*dicts)`

Merges multiple dictionaries into one. Later dictionaries override earlier ones.

**Parameters:**
- `*dicts`: Any number of dictionaries

**Returns:** A new merged dictionary

```python
from toolsed import dict_merge

a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
c = {"x": 999}

merged = dict_merge(a, b)        # → {"x": 1, "y": 99, "z": 3}
merged2 = dict_merge(a, b, c)    # → {"x": 999, "y": 99, "z": 3}
```
---

### `deep_merge(*dicts)`

Recursively merges dictionaries. If values are dictionaries, they are merged; otherwise, later values override earlier ones.

**Parameters:**
- `*dicts`: Any number of dictionaries

**Returns:** A new deeply merged dictionary

```python
from toolsed import deep_merge

a = {"x": 1, "nested": {"a": 1}}
b = {"y": 2, "nested": {"b": 2}}
c = {"z": 3, "nested": {"c": 3}}

merged = deep_merge(a, b)  # → {"x": 1, "y": 2, "nested": {"a": 1, "b": 2}}
deep = deep_merge(a, b, c) # → {"x": 1, "y": 2, "z": 3, "nested": {"a":1, "b":2, "c":3}}

# Non-dict values are overwritten
conflict = deep_merge(
    {"config": {"theme": "dark", "font": "Arial"}},
    {"config": {"theme": "light"}}
)
# → {"config": {"theme": "light", "font": "Arial"}}
