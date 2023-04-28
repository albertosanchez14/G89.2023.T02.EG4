"""Module """
import datetime
import re
import json
from datetime import datetime
from .models.order_delivery import OrderDelivery
from .models.order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .models.order_shipping import OrderShipping
from .order_manager_config import JSON_FILES_PATH
from .singleton_metaclass import SingletonMetaClass


class OrderManager(metaclass=SingletonMetaClass):
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_tracking_code(t_c):
        """Method for validating sha256 values"""
        myregex = re.compile(r"[0-9a-fA-F]{64}$")
        res = myregex.fullmatch(t_c)
        if not res:
            raise OrderManagementException("tracking_code format is not valid")

    @staticmethod
    def save_store(data):
        """Method for saving the orders store"""
        file_store = JSON_FILES_PATH + "orders_store.json"
        # first read the file
        # load
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        # found
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data.order_id:
                found = True
        if found is False:
            data_list.append(data.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        # save
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return True

    @staticmethod
    def save_fast(data):
        """Method for saving the orders store"""
        orders_store = JSON_FILES_PATH + "orders_store.json"
        with open(orders_store, "r+", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
            data_list.append(data.__dict__)
            file.seek(0)
            json.dump(data_list, file, indent=2)

    @staticmethod
    def save_orders_shipped(shipment):
        """Saves the shipping object into a file"""
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        # append the shipments list
        data_list.append(shipment.__dict__)

        try:
            with open(shimpents_store_file, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

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
        """self.validate_tracking_code(tracking_code)

        # check if this tracking_code is in shipments_store
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex
        # search this tracking_code
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")

        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"
        try:
            with open(shipments_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        # append the delivery info
        data_list.append(str(tracking_code))
        data_list.append(str(datetime.utcnow()))
        try:
            with open(shipments_file, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex"""

        order_delivery = OrderDelivery.from_order_tracking_code(tracking_code)
        order_delivery.save_to_store()
        return True
