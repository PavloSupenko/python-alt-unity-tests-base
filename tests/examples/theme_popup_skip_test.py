import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestThemePopupSkip(AltUnityBaseTest):

    def test_enter(self):
        print("Finding close theme popup button")
        openMenuButton = self.altUnityDriver.wait_for_object(By.NAME, 'Exit_Button')
        buttonPosition = openMenuButton.get_screen_position()

        time.sleep(5)

        print("Tap close theme popup button")
        self.altUnityDriver.tap(buttonPosition)

        time.sleep(2)

    def test_exit(self):
        pass
