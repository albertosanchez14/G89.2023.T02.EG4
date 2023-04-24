from abc import ABC, abstractmethod


class Attribute(ABC):
    def __init__(self, value):
        self._value = self.validate(value)

    @abstractmethod
    def validate(self, value):
        pass

    @property
    @abstractmethod
    def value(self):
        return self._value
