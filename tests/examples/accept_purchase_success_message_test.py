import time
from appium.webdriver.common.appiumby import AppiumBy
from tests.base.appium_base_test import AppiumBaseTest


class TestAcceptPurchaseSuccessMessage(AppiumBaseTest):

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
