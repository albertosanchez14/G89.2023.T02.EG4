"Docstring"
import json
from ..order_management_exception import OrderManagementException


class JsonStore:
    _FILE_PATH = ""
    _ID_FIELD = ""

    def __init__(self):
        pass

    @staticmethod
    def empty_store(self):
        """Method for emptying the store"""
        pass
    
    @staticmethod
    def load_store(self):
        """Method for loading the store"""
        file_store = self._FILE_PATH + self._ID_FIELD
        # first read the file
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data_list
    
    @staticmethod
    def save_store(self, data_list):
        """Method for saving the store"""
        file_store = self._FILE_PATH + self._ID_FIELD
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        pass

    @staticmethod
    def add_item(self, item):
        """Method for saving the orders store"""
        orders_store = self._FILE_PATH + self._ID_FIELD
        with open(orders_store, "r+", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
            data_list.append(item.__dict__)
            file.seek(0)
            json.dump(data_list, file, indent=2)

    @staticmethod
    def find_item(self, data_list):
        """Method for finding an item in the store"""
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data.order_id:
                found = True
        if found is False:
            data_list.append(data.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        
