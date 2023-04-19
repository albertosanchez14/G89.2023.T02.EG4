"""Module"""
import re
from ..order_management_exception import OrderManagementException


class Attribute:
    """Docstring"""
    def __init__(self):
        self._attr_value = ""
        self._validation_pattern = r""
        self._error_message = ""

    def _validate(self, value):
        print(self._validation_pattern)
        regex = re.compile(self._validation_pattern)
        res = regex.fullmatch(value)
        if not res:
            raise OrderManagementException(self._error_message)
        return value

    def hola(self):
        """fawdfawf"""
        return None

    @property
    def value(self):
        """adwdawd"""
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        self._attr_value = attr_value
