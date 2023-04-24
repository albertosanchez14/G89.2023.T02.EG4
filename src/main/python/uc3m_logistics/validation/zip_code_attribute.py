from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class ZipCodeAttribute(Attribute):
    def validate(self, attr_value):
        if attr_value.isdigit() and len(attr_value) == 5:
            if int(attr_value) > 52999 or int(attr_value) < 1000:
                raise OrderManagementException("zip_code is not valid")
        else:
            raise OrderManagementException("zip_code format is not valid")
        return attr_value
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, attr_value):
        return self.validate(attr_value)
