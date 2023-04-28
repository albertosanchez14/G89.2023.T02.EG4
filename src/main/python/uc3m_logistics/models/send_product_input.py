"""Docstring for module"""
import json
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.validation.delivery_email_attribute import DeliveryEmailAttribute
from uc3m_logistics.validation.order_id_attribute import OrderIdAttribute


class SendProductInput:
    def __init__(self, order_id: str, delivery_email: str):
        self._order_id = OrderIdAttribute(order_id).value
        self._delivery_email = DeliveryEmailAttribute(delivery_email).value

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = OrderIdAttribute(value).value

    @property
    def email(self):
        return self._delivery_email

    @email.setter
    def email(self, value):
        self._delivery_email = DeliveryEmailAttribute(value).value

    @classmethod
    def from_json(cls, input_file_path: str):
        try:
            with open(input_file_path, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("File is not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        if "OrderID" not in data or "ContactEmail" not in data:
            raise OrderManagementException("Bad label")
        return cls(data["OrderID"], data["ContactEmail"])
