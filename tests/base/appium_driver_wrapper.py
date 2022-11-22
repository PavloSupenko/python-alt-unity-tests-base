import os
from tests.base.account_controller import AccountController
from tests.base.appium_screenshot import AppiumScreenshot
from tests.base.subscription_type import SubscriptionType
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AppiumDriverWrapper:

    def __init__(self, test_artifacts_directory: str):
        is_cloud_run = os.environ["IS_CLOUD_RUN"] == 'true'
        appium_port_number = int(os.environ["APPIUM_PORT"])
        appium_existing_driver = AppiumExistingDriver(appium_port_number)
        self.appium_driver = appium_existing_driver.webDriver
        self.is_ios_platform = appium_existing_driver.isIosPlatform
        self.is_android_platform = appium_existing_driver.isAndroidPlatform
        self.capabilities = appium_existing_driver.capabilities
        self.is_cloud_run = is_cloud_run

        self.screenshooter = AppiumScreenshot(self.appium_driver, test_artifacts_directory)
        self.account = AccountController(self.appium_driver, self.is_ios_platform, self.screenshooter)

        print(f"Cloud status for test run is: {is_cloud_run}")

    def save_screenshot(self, screenshotName):
        self.screenshooter.save(screenshot_name=screenshotName)

    def save_screenshot_with_delay(self, screenshotName: str, delay: int):
        self.screenshooter.delay_and_save(delay=delay, screenshot_name=screenshotName)

    def sign_out_account(self):
        self.account.sign_out()

    def sign_in_account(self, login: str, password: str):
        self.account.sign_in(login=login, password=password)

    def discard_last_subscription(self):
        self.account.discard_last_subscription()

    def wait_subscription(self, subscription_type: SubscriptionType):
        self.account.wait_subscription(subscription_type=subscription_type)
