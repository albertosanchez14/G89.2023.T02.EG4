"""Module """
from .models.order_delivery import OrderDelivery
from .models.order_request import OrderRequest
from .models.order_shipping import OrderShipping
from .singleton_metaclass import SingletonMetaClass


class OrderManager(metaclass=SingletonMetaClass):
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        pass

    # pylint: disable=too-many-arguments
    @staticmethod
    def register_order(product_id,
                       order_type,
                       address,
                       phone_number,
                       zip_code):
        """Register the orders into the order's file"""
        my_order = OrderRequest(product_id,
                                order_type,
                                address,
                                phone_number,
                                zip_code)
        my_order.save_to_store()
        return my_order.order_id

    # pylint: disable=too-many-locals
    @staticmethod
    def send_product(input_file):
        """Sends the order included in the input_file"""
        order_shipping = OrderShipping.from_send_input_file(input_file)
        order_shipping.save_to_store()
        return order_shipping.tracking_code

    @staticmethod
    def deliver_product(tracking_code):
        """Register the delivery of the product"""
        order_delivery = OrderDelivery.from_order_tracking_code(tracking_code)
        order_delivery.save_to_store()
        return True
