import time
from unittest import TestCase
from alttester import By
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestPrivacyPolicySkip(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(enable_alt_unity_tester=True)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        if self.isIosPlatform:
            return

        print("Finding policy accept button")
        acceptButton = self.alt_unity_driver.wait_for_object(By.NAME, 'ButtonOk')

        print("Tap on policy accept button")
        acceptButton.tap()

        self.saveScreenshot("enter")

        time.sleep(3)

    def test_exit(self):
        if self.isIosPlatform:
            return

        print("Finding again policy accept button")
        self.alt_unity_driver.wait_for_object_to_not_be_present(By.NAME, 'ButtonOk')
        self.saveScreenshot("exit")
