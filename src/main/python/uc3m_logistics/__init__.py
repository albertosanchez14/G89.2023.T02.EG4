"""UC3M Care MODULE WITH ALL THE FEATURES REQUIRED FOR ACCESS CONTROL"""

from .order_manager import OrderManager  # pylint: disable=E0401 disable=W0611
from .order_management_exception import OrderManagementException  # pylint: disable=E0401 disable=W0611
from .order_manager_config import JSON_FILES_PATH  # pylint: disable=E0401 disable=W0611
from .order_manager_config import JSON_FILES_RF2_PATH  # pylint: disable=E0401 disable=W0611
from .singleton_metaclass import SingletonMetaClass  # pylint: disable=E0401 disable=W0611
