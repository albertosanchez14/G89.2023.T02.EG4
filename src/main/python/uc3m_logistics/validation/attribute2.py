from abc import ABC, abstractmethod


class Attribute2(ABC):
    def __init__(self, value):
        self.validate(value)
        self._value = value

    @abstractmethod
    def validate(self, value):
        pass

    @property
    def value(self):
        return self._value
