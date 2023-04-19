from .attribute import Attribute


class PhoneNumberAttribute(Attribute):
    def __init__(self, attr_value):
        self._attr_value = self._validate(attr_value)
        self._validation_pattern = r"^(\+)[0-9]{11}"
        self._error_message = "phone number is not valid"

    def validate(self, attr_value):
        super()._validate(attr_value)
        return 0
        
    
    @property
    def value(self):
        return self._value