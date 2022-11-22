import time
from alttester import By
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestThemePopupSkip(AltUnityDriverWrapper):

    def test_enter(self):
        print("Finding close theme popup button")
        openMenuButton = self.alt_unity_driver.wait_for_object(By.NAME, 'Exit_Button')
        buttonPosition = openMenuButton.get_screen_position()

        time.sleep(5)

        print("Tap close theme popup button")
        self.alt_unity_driver.tap(buttonPosition)

        time.sleep(2)

    def test_exit(self):
        pass
