import re
from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException



class PhoneNumberAttribute(Attribute):
    def validate(self, attr_value):
        regex = re.compile(r"^(\+)[0-9]{11}")
        res = regex.fullmatch(attr_value)
        if not res:
            raise OrderManagementException("phone number is not valid")
        return attr_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, attr_value):
        return self.validate(attr_value)
