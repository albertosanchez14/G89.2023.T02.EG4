"Docstring"
import json
from abc import ABC, abstractmethod
from ..order_management_exception import OrderManagementException


class JsonStore(ABC):
    _FILE_PATH = ""

    def __init__(self):
        self.__data = self.load_store()

    def load_store(self):
        """Method for loading the store"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data = []
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data

    def save_store(self):
        """Method for saving the store"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self.__data, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

    @abstractmethod
    def find_item_by_key(self, key):
        pass

    @abstractmethod
    def add_item(self, item):
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        self.save()
