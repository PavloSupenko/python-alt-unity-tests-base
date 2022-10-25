import os
from appium.webdriver.webdriver import WebDriver


class AppiumScreenshot:
    def __init__(self):
        self._test_artifacts_path = os.environ["CUSTOM_CURRENT_TEST_DIR"]
        self._current_screenshot_number = 0

    def save(self, appiumDriver: WebDriver, screenshotName):
        self._current_screenshot_number += 1
        screenshot_path = os.path.join(self._test_artifacts_path, f"{self._current_screenshot_number}.{screenshotName}.png")

        # Create subdirectories if it's needed based on filename
        # It's pretty important to pass directory path as the argument, not file path
        screenshot_directory = os.path.dirname(screenshot_path)
        os.makedirs(screenshot_directory, exist_ok=True)
        print(f"Screenshots save directory: {screenshot_path}")

        screenshot_save_result = appiumDriver.get_screenshot_as_file(screenshot_path)
        print(f"Saving screenshot on path: {screenshot_path} with result: {screenshot_save_result}")
