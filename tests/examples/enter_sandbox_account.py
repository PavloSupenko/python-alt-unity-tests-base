import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from tests.base.appium_base_test import AppiumBaseTest


class TestEnterSandboxAccount(AppiumBaseTest):

    def test_enter(self):
        if self.isAndroidPlatform:
            return

        time.sleep(60)

        appleIdField = self.appiumDriver.find_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeTextField'")
        appleIdField.send_keys("b7551@bb.com")

        passwordField = self.appiumDriver.find_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeSecureTextField'")
        passwordField.send_keys("Qwerty@12345")

        acceptButton = self.appiumDriver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='OK')
        acceptButton.click()

        time.sleep(60)

    def test_exit(self):
        pass
