import os
import unittest
from altunityrunner import AltUnityDriver
from tests.base.appium_screenshot import AppiumScreenshot
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AltUnityBaseTest(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform

        self.altUnityDriver = AltUnityDriver(host="127.0.0.1", port=13000, enable_logging=True, timeout=30)

        # Extract screenshots directory to environment variable in test .sh script
        generalArtifactsDirectory = os.environ['DEVICEFARM_LOG_DIR']
        self.screenshotsSaveDirectory = os.path.join(generalArtifactsDirectory, "Screenshots")
        print(f"Screenshots save directory: {self.screenshotsSaveDirectory}")

    def tearDown(self):
        self.altUnityDriver.stop()

    def saveScreenshot(self, screenshotName):
        AppiumScreenshot(screenshotName).save(self.appiumDriver)
