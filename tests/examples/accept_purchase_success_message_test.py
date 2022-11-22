import time
from unittest import TestCase
from appium.webdriver.common.appiumby import AppiumBy
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestAcceptPurchaseSuccessMessage(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(False)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        if self.isAndroidPlatform:
            return

        accept_button = self.appiumDriver.wait_for_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                           value='OK',
                                                           interval=5,
                                                           timeout=300)
        self.saveScreenshot("purchase_success_message")
        accept_button.click()

    def test_exit(self):
        time.sleep(20)
        self.saveScreenshot("application_purchased")
