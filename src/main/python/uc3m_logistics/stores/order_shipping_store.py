from abc import ABC
from .json_store import JsonStore
from ..order_manager_config import Config
from ..order_management_exception import OrderManagementException


class OrderShippingStore(JsonStore, ABC):
    """Class for managing the order request store"""
    _FILE_PATH = Config.ORDER_SHIPMENTS_STORE_PATH.value

    def find_item_by_key(self, key):
        """Find an item by key"""
        self.data = self.load_store()
        for item in self.data:
            if item["_OrderShipping__tracking_code"] == key:
                return item
        raise OrderManagementException("tracking_code is not found")

    def add_item(self, item):
        """Add an item"""
        self.data = self.load_store()
        self.data.append(item.__dict__)
        self.save_store()
