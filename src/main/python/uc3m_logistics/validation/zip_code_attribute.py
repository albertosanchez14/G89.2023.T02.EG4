from .attribute import Attribute
from ..order_management_exception import OrderManagementException


class ZipCodeAttribute(Attribute):
    def __init__(self, attr_value):
        self._validation_pattern = r"^[0-9]{5}"
        self._error_message = "zip_code format is not valid"
        self._attr_value = self._validate(attr_value)

    def validate(self, attr_value):
        if int(attr_value) > 52999 or int(attr_value) < 1000:
            raise OrderManagementException("zip_code is not valid")
        super()._validate(attr_value)
        return 0
        
    @property
    def value(self):
        return self._attr_value
    
    @value.setter
    def value(self, attr_value):
        return self._validate(attr_value)
