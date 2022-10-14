import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestPurchaseButtonTap(AltUnityBaseTest):

    def test_enter(self):
        print("Finding purchase button")
        purchaseButton = self.altUnityDriver.wait_for_object(By.NAME, 'Button_Subscribe')

        time.sleep(2)

        print("Tap purchase button")
        purchaseButton.tap()

    def test_exit(self):
        pass
