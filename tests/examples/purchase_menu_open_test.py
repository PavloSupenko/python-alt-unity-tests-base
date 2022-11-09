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

        self.saveAnalytics("opened_menu")

    def test_exit(self):
        print("Finding purchase menu close buttons")
        try:
            while True:
                menuCloseButton = self.altUnityDriver.wait_for_object_with_marker(Marker.InApp.MenuCloseButton, timeout=10, interval=2)
                menuCloseButtonName = menuCloseButton.name
                menuCloseButtonParentName = menuCloseButton.get_parent().name

                print(f"Close menu button found on object: {menuCloseButtonName} with parent: {menuCloseButtonParentName}")
                menuCloseButton.tap()

                self.saveScreenshot(f"close.{menuCloseButtonParentName}.{menuCloseButtonName}")
        except:
            print(f"Close button found anymore")
