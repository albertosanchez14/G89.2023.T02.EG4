"""Docstring"""


class SingletonMeta(type):
    _isinstances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._isinstances:
            _isinstance = super().__call__(*args, **kwargs)
            cls._isinstances[cls] = _isinstance
        return cls._isinstances[cls]
