import os
import time
import pytest
from tests.Markers import Marker
from appium.webdriver.common.appiumby import AppiumBy
from tests.base.appium_driver_wrapper import AppiumDriverWrapper
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


@pytest.fixture(scope="module")
def artifacts_path():
    artifacts_directory = os.environ['DEVICEFARM_LOG_DIR']
    test_artifacts_path = os.path.join(artifacts_directory, 'tests', 'purchase_menu_open')
    os.makedirs(test_artifacts_path, exist_ok=True)
    return test_artifacts_path


@pytest.fixture(scope="module")
def appium(artifacts_path):
    baseTestFunctionality = AppiumDriverWrapper(artifacts_path)
    yield baseTestFunctionality
    del baseTestFunctionality


@pytest.fixture()
def alt_unity(artifacts_path):
    baseTestFunctionality = AltUnityDriverWrapper(artifacts_path)
    yield baseTestFunctionality
    del baseTestFunctionality


class TestPurchaseMenuOpen:

    def test_open_purchase_menu(self, skip_onboarding, alt_unity, appium):
        self.open_menu(appium, alt_unity)
        self.close_menu(appium, alt_unity)

    @pytest.fixture
    def launch_application(self, appium):
        appium.appium_driver.activate_app('com.binibambini.drawingforgirls')
        yield
        appium.appium_driver.terminate_app('com.binibambini.drawingforgirls')

    @pytest.fixture
    def skip_firebase_message(self, launch_application, appium):
        if appium.is_android_platform:
            return

        time.sleep(5)

        appium.save_screenshot("enter")

        firebaseWarningSkipButton = appium.appium_driver.find_element_with_multiple_criteria(by=AppiumBy.ACCESSIBILITY_ID, values=['OK', 'Allow', 'Accept'])
        firebaseWarningSkipButton.click()

        time.sleep(2)

    @pytest.fixture
    def skip_onboarding(self, skip_firebase_message, alt_unity, appium):
        alt_unity_driver = alt_unity.alt_unity_driver

        print("Skipping all elements with 'Skip' and 'InApp/Close' markers")

        try:
            while True:
                skipButton = alt_unity_driver.wait_for_object_with_any_marker(target_markers=[Marker.General.Skip, Marker.InApp.MenuCloseButton],
                                                                              timeout=60, interval=2)
                skipButtonName = skipButton.name
                skipButtonParentName = skipButton.get_parent().name

                print(f"Skip button found on object: {skipButtonName} with parent: {skipButtonParentName}")
                skipButton.tap()

                appium.save_screenshot(f"skip.{skipButtonParentName}.{skipButtonName}")
                time.sleep(10)
                alt_unity.save_analytics(f"skip.{skipButtonParentName}.{skipButtonName}")
        except:
            print(f"Skip marker not found anymore")

    def open_menu(self, appium, alt_unity):
        alt_unity_driver = alt_unity.alt_unity_driver
        print("Waiting for purchase menu open button")
        menuOpenButton = alt_unity_driver.wait_for_object_with_marker(Marker.InApp.MenuOpenButton)

        print("Tap purchase menu open button")
        menuOpenButton.tap()

        appium.save_screenshot("open_purchase_menu")
        time.sleep(2)

        appium.save_screenshot("opened_menu")
        time.sleep(2)

        alt_unity.save_analytics("opened_menu")

    def close_menu(self, appium, alt_unity):
        print("Finding purchase menu close buttons")
        alt_unity_driver = alt_unity.alt_unity_driver

        try:
            while True:
                menuCloseButton = alt_unity_driver.wait_for_object_with_marker(Marker.InApp.MenuCloseButton, timeout=10, interval=2)
                menuCloseButtonName = menuCloseButton.name
                menuCloseButtonParentName = menuCloseButton.get_parent().name

                print(f"Close menu button found on object: {menuCloseButtonName} with parent: {menuCloseButtonParentName}")
                menuCloseButton.tap()

                appium.save_screenshot(f"close.{menuCloseButtonParentName}.{menuCloseButtonName}")
        except:
            print(f"Close button found anymore")
