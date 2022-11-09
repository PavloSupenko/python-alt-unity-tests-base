import time
from tests.base.appium_base_test import AppiumBaseTest


class TestReinstallApplication(AppiumBaseTest):

    def test_enter(self):
        self.appiumDriver.remove_app('com.binibambini.acad.drawing')
        time.sleep(5)
        self.appiumDriver.install_app(self.capabilities['app'])

    def test_exit(self):
        pass
