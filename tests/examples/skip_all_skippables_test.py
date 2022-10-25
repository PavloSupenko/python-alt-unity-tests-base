from tests.Markers import Marker
from tests.base.altunity_base_test import AltUnityBaseTest


class TestSkipAllSkippables(AltUnityBaseTest):

    def test_enter(self):
        print("Skipping all elements with 'Skip' marker")

        try:
            while True:
                skipButton = self.altUnityDriver.wait_for_object_with_marker(Marker.General.Skip, timeout=60, interval=1)
                skipButtonName = skipButton.name
                skipButtonParentName = skipButton.get_parent().name

                print(f"Skip button found on object: {skipButtonName} with parent: {skipButtonParentName}")
                skipButton.tap()

                self.saveScreenshot(f"skip.{skipButtonParentName}.{skipButtonName}")
        except:
            print(f"Skip marker not found anymore")

    def test_exit(self):
        pass
