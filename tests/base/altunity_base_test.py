import unittest
from tests.base.appium_screenshot import AppiumScreenshot
from tests.drivers.appium_existing_driver import AppiumExistingDriver
from tests.drivers.custom_alt_unity_driver import CustomAltUnityDriver


class AltUnityBaseTest(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform
        self.screenshooter = AppiumScreenshot()

        self.altUnityDriver = CustomAltUnityDriver(host="127.0.0.1", port=13000, enable_logging=True, timeout=30)

    def tearDown(self):
        self.altUnityDriver.stop()

    def saveScreenshot(self, screenshotName):
        self.screenshooter.save(self.appiumDriver, screenshotName)

