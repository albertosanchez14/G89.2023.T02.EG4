from unittest import TestCase

from uc3m_logistics import OrderManager
from uc3m_logistics.stores import OrderRequestStore, OrderShippingStore, OrderDeliveryStore


class TestSingletonMetaclass(TestCase):
    def test_order_manager_is_singleton(self):
        order_manager1 = OrderManager()
        order_manager2 = OrderManager()
        self.assertEqual(id(order_manager1), id(order_manager2))

    def test_order_request_store_is_singleton(self):
        order_request1 = OrderRequestStore()
        order_request2 = OrderRequestStore()
        self.assertEqual(id(order_request1), id(order_request2))

    def test_order_shipping_store_is_singleton(self):
        order_shipping1 = OrderShippingStore()
        order_shipping2 = OrderShippingStore()
        self.assertEqual(id(order_shipping1), id(order_shipping2))

    def test_order_delivery_store_is_singleton(self):
        order_delivery1 = OrderDeliveryStore()
        order_delivery2 = OrderDeliveryStore()
        self.assertEqual(id(order_delivery1), id(order_delivery2))

    def test_order_manager_is_not_singleton(self):
        order_manager = OrderManager()
        order_request = OrderRequestStore()
        order_shipping = OrderShippingStore()
        order_delivery = OrderDeliveryStore()
        self.assertNotEqual(id(order_manager), id(order_request))
        self.assertNotEqual(id(order_manager), id(order_shipping))
        self.assertNotEqual(id(order_manager), id(order_delivery))

    def test_order_request_store_is_not_singleton(self):
        order_manager = OrderManager()
        order_request = OrderRequestStore()
        order_shipping = OrderShippingStore()
        order_delivery = OrderDeliveryStore()
        self.assertNotEqual(id(order_request), id(order_manager))
        self.assertNotEqual(id(order_request), id(order_shipping))
        self.assertNotEqual(id(order_request), id(order_delivery))

    def test_order_shipping_store_is_not_singleton(self):
        order_manager = OrderManager()
        order_request = OrderRequestStore()
        order_shipping = OrderShippingStore()
        order_delivery = OrderDeliveryStore()
        self.assertNotEqual(id(order_shipping), id(order_manager))
        self.assertNotEqual(id(order_shipping), id(order_request))
        self.assertNotEqual(id(order_shipping), id(order_delivery))

    def test_order_delivery_store_is_not_singleton(self):
        order_manager = OrderManager()
        order_request = OrderRequestStore()
        order_shipping = OrderShippingStore()
        order_delivery = OrderDeliveryStore()
        self.assertNotEqual(id(order_delivery), id(order_manager))
        self.assertNotEqual(id(order_delivery), id(order_request))
        self.assertNotEqual(id(order_delivery), id(order_shipping))