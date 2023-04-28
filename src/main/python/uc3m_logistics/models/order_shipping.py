"""Contains the class OrderShipping"""
import hashlib
import datetime
from datetime import datetime
from uc3m_logistics.models.send_product_input import SendProductInput
from uc3m_logistics.stores.order_request_store import OrderRequestStore
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore
from uc3m_logistics.validation.delivery_email_attribute import DeliveryEmailAttribute
from uc3m_logistics.validation.order_id_attribute import OrderIdAttribute
from uc3m_logistics.validation.product_id_attribute import ProductIdAttribute


# pylint: disable=too-many-instance-validation
class OrderShipping:
    """Class representing the shipping of an order"""

    def __init__(self, product_id, order_id, delivery_email, order_type):
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__product_id = ProductIdAttribute(product_id).value
        self.__order_id = OrderIdAttribute(order_id).value
        self.__delivery_email = DeliveryEmailAttribute(delivery_email).value
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if order_type == "Regular":
            delivery_days = 7
        else:
            delivery_days = 1
        # timestamp is represneted in seconds.microseconds
        # __delivery_day must be expressed in senconds to be added to the timestap
        self.__delivery_day = self.__issued_at + (delivery_days * 24 * 60 * 60)
        self.__tracking_code = hashlib.sha256(self.__signature_string().encode()).hexdigest()

    def __signature_string(self):
        """Composes the string to be used for generating the tracking_code"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",order_id:" + \
            self.__order_id + ",issuedate:" + str(self.__issued_at) + \
            ",deliveryday:" + str(self.__delivery_day) + "}"

    def save_to_store(self):
        """Method for saving the order request to the store"""
        OrderShippingStore().add_item(self)

    @classmethod
    def from_send_input_file(cls, input_file_path: str):
        """Class method for creating an instance of OrderShipping from the input file"""
        send_product_input = SendProductInput.from_json(input_file_path)
        order_request = OrderRequestStore().find_item_by_key(send_product_input.order_id)
        return cls(product_id=order_request.product_id,
                   order_id=send_product_input.order_id,
                   order_type=order_request.order_type,
                   delivery_email=send_product_input.email)

    @property
    def product_id(self):
        """Property representing the products  EAN13 code"""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = ProductIdAttribute(value).value

    @property
    def order_id(self):
        """Property that represents the order_id"""
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id = OrderIdAttribute(value).value

    @property
    def email(self):
        """Property that represents the email of the client"""
        return self.__delivery_email

    @email.setter
    def email(self, value):
        self.__delivery_email = DeliveryEmailAttribute(value).value

    @property
    def tracking_code(self):
        """returns the tracking code"""
        return self.__tracking_code

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value

    @property
    def delivery_day(self):
        """Returns the delivery day for the order"""
        return self.__delivery_day
