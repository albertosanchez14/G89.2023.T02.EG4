from .attribute import Attribute


class DeliveryAddressAttribute(Attribute):
    def __init__(self, attr_value):
        self._validation_pattern = r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$"
        self._error_message = "address is not valid"
        self._attr_value = self._validate(attr_value)

    def validate(self, attr_value):
        super()._validate(attr_value)
        return 0
        
    
    @property
    def value(self):
        return self._attr_value
