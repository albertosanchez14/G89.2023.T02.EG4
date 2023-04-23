from .attribute import Attribute
from ..order_management_exception import OrderManagementException


class ProductIdAttribute(Attribute):
    def __init__(self, attr_value):
        self._validation_pattern = r"^[0-9]{13}$"
        self._error_message = "Invalid EAN13 code string"
        self._attr_value = self._validate(attr_value)

    def validate(self, attr_value):
        """Validate the attribute value"""
        checksum = 0
        code_read = -1
        res = False

        super()._validate(attr_value)

        for i, digit in enumerate(reversed(attr_value)):
            try:
                current_digit = int(digit)
            except ValueError as v_e:
                raise OrderManagementException("Invalid EAN13 code string") from v_e
            if i == 0:
                code_read = current_digit
            else:
                checksum += (current_digit) * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read != -1) and (code_read == control_digit):
            res = True
        else:
            raise OrderManagementException("Invalid EAN13 control digit")
        return res

    @property
    def value(self):
        return self._attr_value
    
    @value.setter
    def value(self, attr_value):
        return self._validate(attr_value)
