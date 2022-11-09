import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from tests.base.appium_screenshot import AppiumScreenshot
from tests.base.subscription_type import SubscriptionType
from tests.drivers.custom_appium_driver import CustomAppiumDriver


class AccountController:
    subscription_type_to_time_ios = {
        SubscriptionType.Week: 3,
        SubscriptionType.Month: 5,
        SubscriptionType.MonthX2: 10,
        SubscriptionType.MonthX3: 15,
        SubscriptionType.MonthX6: 30,
        SubscriptionType.Year: 60
    }

    subscription_type_to_time_android = {
        SubscriptionType.FreeTrial: 3,
        SubscriptionType.Week: 5,
        SubscriptionType.Month: 5,
        SubscriptionType.MonthX3: 10,
        SubscriptionType.MonthX6: 15,
        SubscriptionType.Year: 30
    }

    def __init__(self, appium_driver: CustomAppiumDriver, is_ios_platform: bool, screenshoter: AppiumScreenshot):
        self._is_ios_platform = is_ios_platform
        self._driver = appium_driver
        self._screenshoter = screenshoter

    def sign_out(self):
        if self._is_ios_platform:
            self._sign_out_ios()
        else:
            self._sign_out_android()

    def sign_in(self, login: str, password: str):
        self._close_settings_ios()
        self._try_sign_out_ios()
        self._close_settings_ios()

        if self._is_ios_platform:
            self._sign_in_ios(login, password)
        else:
            self._sign_in_android(login, password)

        self._close_settings_ios()

    def wait_subscription(self, subscription_type: SubscriptionType):
        if self._is_ios_platform:
            waiting_time_in_minutes = self.subscription_type_to_time_ios[subscription_type]
        else:
            waiting_time_in_minutes = self.subscription_type_to_time_android[subscription_type]

        waiting_time_in_seconds = waiting_time_in_minutes * 60
        time.sleep(waiting_time_in_seconds)

    def discard_last_subscription(self):
        # Open 'manage' tab in account settings
        self._open_account_settings_tab_ios('Manage')
        self._screenshoter.delay_and_save(2, "account_manage_tab")

        self._try_retry_button_click_ios()
        self._try_open_last_subscription_settings_ios()
        self._try_retry_button_click_ios()

        # tap 'Cancel Subscription' button by ID
        cancel_button = self._driver.wait_for_element(by=MobileBy.ACCESSIBILITY_ID, value='Cancel Subscription', interval=5, timeout=60)
        # Cancel button does not work with click. Not sure why. We are using click function to focus on this button
        cancel_button.click()
        time.sleep(2)
        actions = TouchAction(self._driver)
        actions.tap(cancel_button)
        actions.perform()

        self._screenshoter.delay_and_save(2, "cancelling_subscription")

        # tap 'Confirm' button by id
        confirm_button = self._driver.wait_for_element(by=MobileBy.ACCESSIBILITY_ID, value='Confirm', interval=5, timeout=60)
        confirm_button.click()
        self._screenshoter.delay_and_save(2, "confirm_cancelling")

        self._close_settings_ios()

    def _try_sign_out_ios(self):
        try:
            self.sign_out()
        except:
            print('No account to sign out found.')

    def _sign_out_ios(self):
        self._open_account_settings_tab_ios('Sign Out')
        self._screenshoter.delay_and_save(2, "account_signed_out")

    def _sign_in_ios(self, login: str, password: str):
        self._open_app_store_settings_ios()

        # Click Sign In button
        sign_out_button = self._driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='Sign In')
        sign_out_button.click()
        self._screenshoter.delay_and_save(2, "account_sign_in_button")

        # Entering account login and password
        acceptButton = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Sign In')
        appleIdField = self._driver.find_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeTextField'")
        appleIdField.send_keys(login)

        # On iPadOS 15.5 there is only login field and password appears only after 'Sign In' button down
        try:
            passwordField = self._driver.find_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeSecureTextField'")
        except:
            print('Password field not found. Trying to click on Sign in button and then pass password.')
            acceptButton.click()
            passwordField = self._driver.wait_for_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeSecureTextField'")
            acceptButton = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Sign In')

        passwordField.send_keys(password)

        acceptButton.click()
        self._screenshoter.delay_and_save(2, "waiting_account_connection")

        # Click Other options button on upgrade program menu
        other_options_button = self._driver.wait_for_element(by=AppiumBy.ACCESSIBILITY_ID, value='Other options', timeout=300, interval=10)
        self._screenshoter.delay_and_save(2, "account_connected")
        other_options_button.click()
        self._screenshoter.delay_and_save(2, "other_options")

        # Click Do not upgrade option
        not_upgrade_button = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Do not upgrade')
        not_upgrade_button.click()

        self._driver.wait_for_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeStaticText' AND name CONTAINS 'Apple ID:'", timeout=300, interval=10)
        self._screenshoter.save("account_entered")

    def _sign_out_android(self):
        pass

    def _sign_in_android(self, login: str, password: str):
        pass

    def _open_app_store_settings_ios(self):
        # Open device settings app
        self._driver.activate_app('com.apple.Preferences')
        self._screenshoter.delay_and_save(2, "settings_opened")

        # Open App Store settings
        app_store_button = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='App Store')
        app_store_button.click()
        self._screenshoter.delay_and_save(2, "app_store_settings_opened")

    def _open_account_settings_ios(self):
        self._open_app_store_settings_ios()

        account_button = self._driver.find_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeStaticText' AND name CONTAINS 'Apple ID'")
        account_button.click()
        self._screenshoter.delay_and_save(2, "account_settings_opened")

    def _open_account_settings_tab_ios(self, tab_name: str):
        self._open_account_settings_ios()
        sign_out_button = self._driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=tab_name)
        sign_out_button.click()

    def _close_settings_ios(self):
        self._driver.terminate_app('com.apple.Preferences')

    def _try_open_last_subscription_settings_ios(self):
        # find by name contains 'Next billing date'. type=button
        try:
            subscription_button = self._driver.wait_for_element(by=MobileBy.IOS_PREDICATE,
                                                            value="type == 'XCUIElementTypeButton' AND (name CONTAINS 'Next billing date' OR name CONTAINS 'Expires')",
                                                            interval=10, timeout=100)
            self._screenshoter.delay_and_save(2, "subscriptions_list")
            subscription_button.click()
        except:
            print(f"Subscriptions list not found. It can be caused if there is only one subscription on account and it's opening concrete subscription immediate")

    def _try_retry_button_click_ios(self):
        try:
            retry_button = self._driver.wait_for_element(by=MobileBy.IOS_PREDICATE, value="type == 'XCUIElementTypeButton' AND name CONTAINS 'Retry'",
                                                         interval=10, timeout=60)

            print('Retry button found.')
            self._screenshoter.delay_and_save(2, "retry_button")
            retry_button.click()
        except:
            print(f"No Retry button found.")
