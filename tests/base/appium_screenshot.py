import os
from datetime import datetime
from appium.webdriver.webdriver import WebDriver


class AppiumScreenshot:
    def __init__(self, screenshotName):
        screenshotsDirectoryPath = os.environ['CUSTOM_SCREENSHOTS_DIR']
        screenshotFullPath = os.path.join(screenshotsDirectoryPath, f"{screenshotName}.png")

        currentTime = datetime.now().strftime("%H:%M:%S")
        screenshotDirectory = os.path.dirname(screenshotFullPath)
        newScreenshotFilename = f"[{currentTime}] {os.path.basename(screenshotFullPath)}"

        # Create subdirectories if it's needed based on filename
        os.makedirs(screenshotDirectory, exist_ok=True)

        newScreenshotFullPath = os.path.join(screenshotDirectory, newScreenshotFilename)
        self.screenshotPath = newScreenshotFullPath

        print(f"Screenshots save directory: {newScreenshotFullPath}")

    def save(self, appiumDriver: WebDriver):
        screenshotSaveResult = appiumDriver.get_screenshot_as_file(self.screenshotPath)
        print(f"Saving screenshot on path: {self.screenshotPath} with result: {screenshotSaveResult}")
