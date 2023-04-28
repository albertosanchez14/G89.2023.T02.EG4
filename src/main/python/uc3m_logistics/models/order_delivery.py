"""Docstring for this file"""
from datetime import datetime

from uc3m_logistics import OrderManagementException
from uc3m_logistics.stores.order_delivery_store import OrderDeliveryStore
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore
from uc3m_logistics.validation.tracking_code_attribute import TrackingCodeAttribute


class OrderDelivery:
    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCodeAttribute(tracking_code).value
        self.__delivery_day = str(datetime.utcnow())

    @property
    def tracking_code(self):
        return self.__tracking_code

    @tracking_code.setter
    def tracking_code(self, value):
        self.__tracking_code = TrackingCodeAttribute(value).value

    def save_to_store(self):
        """Method for saving the order request to the store"""
        OrderDeliveryStore().add_item(self)

    @staticmethod
    def from_order_tracking_code(tracking_code):
        """Class method for creating an instance of OrderShipping from the input file"""
        TrackingCodeAttribute(tracking_code)
        order_shipping = OrderShippingStore().find_item_by_key(tracking_code)
        if not order_shipping:
            raise OrderManagementException("tracking_code is not found")
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(order_shipping["_OrderShipping__delivery_day"]).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
        return order_shipping
