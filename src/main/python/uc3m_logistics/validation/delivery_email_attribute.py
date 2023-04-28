import re
from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class DeliveryEmailAttribute(Attribute):
    def validate(self, attr_value):
        regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'
        regex = re.compile(regex_email)
        res = regex.fullmatch(attr_value)
        if not res:
            raise OrderManagementException("contact email is not valid")
        return attr_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, attr_value):
        return self.validate(attr_value)
