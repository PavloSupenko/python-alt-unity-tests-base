import time
from unittest import TestCase
from tests.Markers import Marker
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestPurchaseButtonTap(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(enable_alt_unity_tester=True)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        print("Waiting for purchase menu open button")
        purchaseButton = self.alt_unity_driver.wait_for_object_with_marker(Marker.InApp.InMenuPurchaseButton, timeout=10)

        time.sleep(2)

        print("Tap purchase menu open button")
        purchaseButton.tap()

        self.saveScreenshot("tap_purchase_button")
        time.sleep(2)

        self.saveScreenshot("purchase_button_tap_result")
        time.sleep(2)

        self.save_analytics("tap_purchase_button")

    def test_exit(self):
        pass
