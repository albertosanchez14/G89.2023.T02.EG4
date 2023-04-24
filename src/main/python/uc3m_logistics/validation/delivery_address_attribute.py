import re
from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class DeliveryAddressAttribute(Attribute):
    def validate(self, attr_value):
        regex = re.compile(r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$")
        res = regex.fullmatch(attr_value)
        if not res:
            raise OrderManagementException("address is not valid")
        return attr_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, attr_value):
        return self.validate(attr_value)
