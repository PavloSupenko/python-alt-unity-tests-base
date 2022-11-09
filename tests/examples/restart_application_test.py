import time
from tests.base.appium_base_test import AppiumBaseTest


class TestRestartApplication(AppiumBaseTest):

    def test_enter(self):
        self.appiumDriver.terminate_app('com.binibambini.acad.drawing')
        time.sleep(5)
        self.appiumDriver.activate_app('com.binibambini.acad.drawing')

    def test_exit(self):
        pass
