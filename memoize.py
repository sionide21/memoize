from functools import wraps


def mproperty(fn):
    attribute = "_memo_%s" % fn.__name__

    @property
    @wraps(fn)
    def _property(self):
        if not hasattr(self, attribute):
            setattr(self, attribute, fn(self))
        return getattr(self, attribute)

    return _property
