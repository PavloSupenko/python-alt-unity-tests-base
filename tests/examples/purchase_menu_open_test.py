import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestPurchaseMenuOpen(AltUnityBaseTest):

    def test_enter(self):
        print("Finding open purchase menu button")
        openMenuButton = self.altUnityDriver.wait_for_object(By.NAME, 'Subscribe')

        time.sleep(5)

        print("Tap open purchase menu button")
        openMenuButton.tap()

        time.sleep(10)

    def test_exit(self):
        pass
