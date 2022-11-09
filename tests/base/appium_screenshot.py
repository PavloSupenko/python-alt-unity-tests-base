import os
import time
from appium.webdriver.webdriver import WebDriver


class AppiumScreenshot:
    def __init__(self, appium_driver: WebDriver, path: str):
        self._test_artifacts_path = path
        self._current_screenshot_number = 0
        self._driver = appium_driver

    def save(self, screenshot_name: str):
        self._current_screenshot_number += 1
        screenshot_path = os.path.join(self._test_artifacts_path, f"{self._current_screenshot_number}.{screenshot_name}.png")

        # Create subdirectories if it's needed based on filename
        # It's pretty important to pass directory path as the argument, not file path
        screenshot_directory = os.path.dirname(screenshot_path)
        os.makedirs(screenshot_directory, exist_ok=True)
        print(f"Screenshots save directory: {screenshot_path}")

        screenshot_save_result = self._driver.get_screenshot_as_file(screenshot_path)
        print(f"Saving screenshot on path: {screenshot_path} with result: {screenshot_save_result}")

    def delay_and_save(self, delay: int, screenshot_name: str):
        time.sleep(delay)
        self.save(screenshot_name)
