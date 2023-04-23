from .attribute import Attribute


class OrderTypeAttribute(Attribute):
    def __init__(self, attr_value):
        self._validation_pattern = r"(Regular|Premium)"
        self._error_message = "order_type is not valid"
        self._attr_value = self._validate(attr_value)

    def validate(self, attr_value):
        super()._validate(attr_value)
        return 0
    
    @property
    def value(self):
        return self._attr_value
