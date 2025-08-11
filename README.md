# `toolsed` — Simple, Practical Utilities for Python

**`toolsed`** is a lightweight library that provides practical, reusable functions for everyday Python programming. It eliminates common boilerplate and makes code more readable.

No magic. No dependencies. Just useful tools you'd write yourself — but already tested and ready to use.

---

## 🚀 Why `toolsed`?

You've probably written these helpers dozens of times:
- Get the first item from a list (or return `None`)
- Safely access nested dicts
- Flatten a list of lists
- Truncate long strings
- Handle optional values gracefully

`toolsed` collects them into one clean, reliable package.

---

## 📦 Installation

```bash
pip install toolsed
```

Or install locally for development:

```bash
pip install -e .
```

---

## 🧩 Quick Example

```python
from toolsed import first, safe_get, truncate, pluralize

first([1, 2, 3])                           # → 1
safe_get({"a": {"b": 42}}, "a", "b")       # → 42
truncate("Hello world", 8)                 # → "Hello..."
pluralize(5, "file")                       # → "5 files"
```

---

## 📚 Full Documentation

See detailed docs for each module:
- [`dicttools.md`](docs/dicttools.md) — Dictionary utilities
- [`functions.md`](docs/functions.md) — Core utilities
- [`listtools.md`](docs/listtools.md) — List and iterable tools
- [`stringtools.md`](docs/stringtools.md) — String formatting

---

## 🛠️ Development

To contribute:
```bash
git clone https://github.com/your-username/toolsed
cd toolsed
pip install -e .
pytest
```

---

## 📄 License

MIT
```

---
