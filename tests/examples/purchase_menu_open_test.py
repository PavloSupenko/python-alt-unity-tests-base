import time
from tests.Markers import Marker
from tests.base.altunity_base_test import AltUnityBaseTest


class TestPurchaseMenuOpen(AltUnityBaseTest):

    def test_enter(self):
        print("Waiting for purchase menu open button")
        menuOpenButton = self.altUnityDriver.wait_for_object_with_marker(Marker.InApp.MenuOpenButton)

        print("Tap purchase menu open button")
        menuOpenButton.tap()

        self.saveScreenshot("open_purchase_menu")
        time.sleep(2)

        self.saveScreenshot("opened_menu")
        time.sleep(2)

    def test_exit(self):
        print("Finding purchase menu close button")
        menuCloseButton = self.altUnityDriver.wait_for_object_with_marker(Marker.InApp.MenuCloseButton)

        print("Tap purchase menu close button")
        menuCloseButton.tap()

        self.saveScreenshot("close_purchase_menu")
