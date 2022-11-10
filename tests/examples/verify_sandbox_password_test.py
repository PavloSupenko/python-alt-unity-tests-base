from appium.webdriver.common.mobileby import MobileBy
from tests.base.appium_base_test import AppiumBaseTest


class TestVerifySandboxPassword(AppiumBaseTest):

    def test_enter(self):
        if self.isAndroidPlatform:
            return

        password_field = self.appiumDriver.wait_for_element(by=MobileBy.IOS_PREDICATE,
                                                            value="type == 'XCUIElementTypeSecureTextField'",
                                                            timeout=300,
                                                            interval=5)
        self.saveScreenshot("verifying_window")
        password_field.send_keys("Qwerty@12345")
        password_field_y = password_field.location['y']

        buttons = self.appiumDriver.find_elements(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeButton'")
        if buttons is None or len(buttons) == 0:
            print('No native buttons found.')
            return

        most_closed_button = None
        most_closed_button_y = 0

        for button in buttons:
            button_attribute_y = button.location['y']
            button_y = int(button_attribute_y)

            if abs(button_y - password_field_y) < abs(most_closed_button_y - password_field_y):
                most_closed_button_y = button_y
                most_closed_button = button

        button_text = most_closed_button.get_attribute('name')
        print(f"Found next to password field button with text: {button_text} and Y-position: {most_closed_button_y} when password Y-position: {password_field_y}")

        most_closed_button.click()

    def test_exit(self):
        pass
