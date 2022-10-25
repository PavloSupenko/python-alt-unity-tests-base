import unittest
from tests.base.appium_screenshot import AppiumScreenshot
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AppiumBaseTest(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform
        self.screenshooter = AppiumScreenshot()

    def saveScreenshot(self, screenshotName):
        self.screenshooter.save(self.appiumDriver, screenshotName)
