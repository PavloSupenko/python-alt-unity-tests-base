import time
from unittest import TestCase
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestLaunchApplication(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(False)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        self.appiumDriver.activate_app('com.binibambini.acad.drawing')
        time.sleep(5)
        self.saveScreenshot("launched_application")

    def test_exit(self):
        pass
