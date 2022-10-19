import os
from appium.webdriver.webdriver import WebDriver


class AppiumScreenshot:
    def __init__(self, screenshotName):
        test_artifacts_path = os.environ["CUSTOM_CURRENT_TEST_DIR"]
        self.screenshot_path = os.path.join(test_artifacts_path, f"{screenshotName}.png")

        # Create subdirectories if it's needed based on filename
        # It's pretty important to pass directory path as the argument, not file path
        screenshot_directory = os.path.dirname(self.screenshot_path)
        os.makedirs(screenshot_directory, exist_ok=True)
        print(f"Screenshots save directory: {self.screenshot_path}")

    def save(self, appiumDriver: WebDriver):
        screenshot_save_result = appiumDriver.get_screenshot_as_file(self.screenshot_path)
        print(f"Saving screenshot on path: {self.screenshot_path} with result: {screenshot_save_result}")
