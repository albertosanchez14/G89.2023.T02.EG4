from json_store import JSONStore


class OrderRequestStore(JSONStore):
    """Class for managing the order request store"""
    _FILE_PATH = "JSON_FILES_PATH"
    
    def find_item_by_key(self, key):
        """Find an item by key"""
        for item in self.data:
            if item[OrderRequestKeys.ID.value] == key:
        

    def add_item(self, item):
        """Add an item"""
        self.data.append(item.__dict__)
        self.save_store()
