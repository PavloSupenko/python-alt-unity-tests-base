from appium.webdriver.common.mobileby import MobileBy
from tests.base.appium_base_test import AppiumBaseTest


class TestDoPurchase(AppiumBaseTest):

    def test_enter(self):
        if self.isAndroidPlatform:
            return

        button = self.appiumDriver.wait_for_element(by=MobileBy.IOS_PREDICATE,
                                                    value="type == 'XCUIElementTypeButton' AND (name CONTAINS 'Subscribe' OR name CONTAINS 'Purchase')",
                                                    interval=10,
                                                    timeout=300)
        self.saveScreenshot("accepting_native_purchase_menu")
        button.click()

    def test_exit(self):
        pass
