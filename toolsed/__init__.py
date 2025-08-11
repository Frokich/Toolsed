# toolsed/__init__.py

from .functions import first, last, noop, always, is_iterable
from .listtools import flatten, compact, ensure_list, chunks
from .dicttools import safe_get, dict_merge
from .stringtools import truncate, pluralize

__all__ = [
    'first', 'last', 'noop', 'always', 'is_iterable',
    'flatten', 'compact', 'ensure_list', 'chunks',
    'safe_get', 'dict_merge',
    'truncate', 'pluralize'
    ]

__version__ = "0.1.0"
__author__ = "Froki"
__email__ = "iroorp32@gmail.com"
