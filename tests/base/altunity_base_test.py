import os
import unittest
from tests.base.account_controller import AccountController
from tests.base.altunity_analytics import AltUnityAnalytics
from tests.base.appium_screenshot import AppiumScreenshot
from tests.base.subscription_type import SubscriptionType
from tests.drivers.appium_existing_driver import AppiumExistingDriver
from tests.drivers.custom_alt_unity_driver import CustomAltUnityDriver


class AltUnityBaseTest(unittest.TestCase):

    def setUp(self):
        alt_unity_port_number = int(os.environ["ALT_UNITY_PORT"])
        self.altUnityDriver = CustomAltUnityDriver(host="127.0.0.1", enable_logging=True, timeout=30, port=alt_unity_port_number)
        self.analytics = AltUnityAnalytics(alt_unity_driver=self.altUnityDriver,
                                           path=os.environ["CUSTOM_CURRENT_TEST_DIR"],
                                           class_name='Bini.Drawing.AnalyticsReader.EventsReader',
                                           assembly='Bini.Drawing.AnalyticsReader',
                                           method='GetLastAnalyticsEvents')

        # Appium base test functionality
        is_cloud_run = os.environ["IS_CLOUD_RUN"] == 'true'
        appium_port_number = int(os.environ["APPIUM_PORT"])
        appium_existing_driver = AppiumExistingDriver(appium_port_number)
        self.appiumDriver = appium_existing_driver.webDriver
        self.isIosPlatform = appium_existing_driver.isIosPlatform
        self.isAndroidPlatform = appium_existing_driver.isAndroidPlatform
        self.capabilities = appium_existing_driver.capabilities
        self.isCloudRun = is_cloud_run

        self.screenshooter = AppiumScreenshot(self.appiumDriver, os.environ["CUSTOM_CURRENT_TEST_DIR"])
        self.account = AccountController(self.appiumDriver, self.isIosPlatform, self.screenshooter)

        print(f"Cloud status for test run is: {is_cloud_run}")

    def tearDown(self):
        self.altUnityDriver.stop()

    def saveAnalytics(self, fileName):
        self.analytics.save(file_name=fileName)

    def getNewAnalytics(self):
        return self.analytics.get_analytics_data()

    def saveScreenshot(self, screenshotName):
        self.screenshooter.save(screenshot_name=screenshotName)

    def saveScreenshotOnDelay(self, screenshotName: str, delay: int):
        self.screenshooter.delay_and_save(delay=delay, screenshot_name=screenshotName)

    def signOutAccount(self):
        self.account.sign_out()

    def signInAccount(self, login: str, password: str):
        self.account.sign_in(login=login, password=password)

    def discardLastSubscription(self):
        self.account.discard_last_subscription()

    def waitSubscription(self, subscription_type: SubscriptionType):
        self.account.wait_subscription(subscription_type=subscription_type)
