import datetime
from datetime import datetime
from abc import ABC
from freezegun import freeze_time
from .json_store import JsonStore
from ..order_manager_config import Config
from ..order_management_exception import OrderManagementException


class OrderRequestStore(JsonStore, ABC):
    """Class for managing the order request store"""
    _FILE_PATH = Config.ORDER_REQUESTS_STORE_PATH.value

    def find_item_by_key(self, key: str):
        """Find an item by key"""
        self.data = self.load_store()
        found = False
        found_item: dict or None = None
        for item in self.data:
            if item["_OrderRequest__order_id"] == key:
                found = True
                found_item = item
                break
        if found:
            # retrieve the orders data
            proid = found_item["_OrderRequest__product_id"]
            address = found_item["_OrderRequest__delivery_address"]
            reg_type = found_item["_OrderRequest__order_type"]
            phone = found_item["_OrderRequest__phone_number"]
            order_timestamp = found_item["_OrderRequest__time_stamp"]
            zip_code = found_item["_OrderRequest__zip_code"]
            # set the time when the order was registered for checking the md5
            with freeze_time(datetime.fromtimestamp(order_timestamp).date()):
                from uc3m_logistics.models.order_request import OrderRequest
                order = OrderRequest(product_id=proid,
                                     delivery_address=address,
                                     order_type=reg_type,
                                     phone_number=phone,
                                     zip_code=zip_code)
            if order.order_id != found_item["_OrderRequest__order_id"]:
                raise OrderManagementException("Orders' data have been manipulated")
            if not found:
                raise OrderManagementException("order_id not found")
            return order

    def add_item(self, new_item):
        """Add an item"""
        self.data = self.load_store()
        found = False
        for item in self.data:
            if item["_OrderRequest__order_id"] == new_item.order_id:
                found = True
        if not found:
            self.data.append(new_item.__dict__)
            self.save_store()
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
