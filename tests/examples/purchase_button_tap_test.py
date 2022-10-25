import time
from tests.Markers import Marker
from tests.base.altunity_base_test import AltUnityBaseTest


class TestPurchaseButtonTap(AltUnityBaseTest):

    def test_enter(self):
        print("Waiting for purchase menu open button")
        purchaseButton = self.altUnityDriver.wait_for_object_with_marker(Marker.InApp.InMenuPurchaseButton, timeout=10)

        time.sleep(2)

        print("Tap purchase menu open button")
        purchaseButton.tap()

        self.saveScreenshot("tap_purchase_button")
        time.sleep(2)

        self.saveScreenshot("purchase_button_tap_result")
        time.sleep(2)

    def test_exit(self):
        pass
