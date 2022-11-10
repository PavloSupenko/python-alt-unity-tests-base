import time
from tests.base.appium_base_test import AppiumBaseTest


class TestLaunchApplication(AppiumBaseTest):

    def test_enter(self):
        self.appiumDriver.activate_app('com.binibambini.acad.drawing')
        time.sleep(5)
        self.saveScreenshot("launched_application")

    def test_exit(self):
        pass
