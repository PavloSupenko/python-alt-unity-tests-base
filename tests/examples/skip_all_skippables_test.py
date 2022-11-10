import time
from tests.Markers import Marker
from tests.base.altunity_base_test import AltUnityBaseTest


class TestSkipAllSkippables(AltUnityBaseTest):

    def test_enter(self):
        print("Skipping all elements with 'Skip' and 'InApp/Close' markers")

        try:
            while True:
                skipButton = self.altUnityDriver.wait_for_object_with_any_marker(target_markers=[Marker.General.Skip, Marker.InApp.MenuCloseButton],
                                                                                 timeout=60, interval=2)
                skipButtonName = skipButton.name
                skipButtonParentName = skipButton.get_parent().name

                print(f"Skip button found on object: {skipButtonName} with parent: {skipButtonParentName}")
                skipButton.tap()

                self.saveScreenshot(f"skip.{skipButtonParentName}.{skipButtonName}")
                time.sleep(10)
                self.saveAnalytics(f"skip.{skipButtonParentName}.{skipButtonName}")
        except:
            print(f"Skip marker not found anymore")

    def test_exit(self):
        pass
