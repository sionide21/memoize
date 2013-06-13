Memoize
=======

Only compute the value of properties the first time they are called. The easiest way to explain it is by example.

#### Bad
```python
class Foo(object):
    def __init__(self):
        self._bar_cache = None

    @property
    def bar(self):
        if self._bar_cache is None:
            self._bar_cache = 2 * 2 * 2
        return self._bar_cache
```


#### Good
```python
from memoize import mproperty

class Foo(object):
    @mproperty
    def bar(self):
        return 2 * 2 * 2
```


## Installation

This package is available on pypi. Installation is as simple as:

    pip install memoize
