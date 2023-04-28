from abc import ABC
from .json_store import JsonStore
from ..order_manager_config import Config


class OrderDeliveryStore(JsonStore, ABC):
    """Class for managing the order request store"""
    _FILE_PATH = Config.ORDER_DELIVERS_STORE_PATH.value

    def find_item_by_key(self, key: str):
        """Find an item by key"""
        """for item in self.data:
            if item[OrderRequestKeys.ID.value] == key:
                return item
        return None"""
        self.data = self.load_store()
        pass

    def add_item(self, item):
        """Add an item"""
        self.data = self.load_store()
        self.data.append(item.__dict__)
        self.save_store()
