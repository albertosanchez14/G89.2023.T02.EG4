import re
from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class OrderIdAttribute(Attribute):
    def validate(self, attr_value):
        myregex = re.compile(r"[0-9a-fA-F]{32}$")
        res = myregex.fullmatch(attr_value)
        if not res:
            raise OrderManagementException("order id is not valid")
        return attr_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, attr_value):
        return self.validate(attr_value)
