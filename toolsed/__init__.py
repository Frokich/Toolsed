# toolsed/__init__.py

from .functions import (first, last, noop, always, is_iterable,
    iden, tap, lmap, lfilter, truthy, falsy,)
from .listtools import (flatten, compact, ensure_list, chunks, without, dedupe,
    )
from .dicttools import (safe_get, dict_merge, deep_merge, pick, omit
    )
from .stringtools import (truncate, pluralize, slugify,
    )

__all__ = [
    'first', 'last', 'noop', 'always', 'is_iterable' ,
    'iden', 'tap', 'lmap', 'lfilter', 'truthy', 'dedupe', 'pick', 'omit', 'slugify', 'falsy',
    'flatten', 'compact', 'ensure_list', 'chunks', 'without', 'deep_merge',
    'safe_get', 'dict_merge',
    'truncate', 'pluralize'
    ]

__version__ = "0.3.0"
__author__ = "Froki"
__email__ = "iroorp32@gmail.com"
