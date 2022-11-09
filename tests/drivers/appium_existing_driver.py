import json
import os
import sys
import requests
from tests.drivers.custom_appium_driver import CustomAppiumDriver

sys.path.append(os.path.dirname(__file__))


class AppiumExistingDriver:
    webDriver = None
    platform = None
    isIosPlatform = False
    isAndroidPlatform = False
    capabilities = None

    def __init__(self, appium_port: int):
        appiumUrl = f"http://localhost:{appium_port}/wd/hub"
        content = requests.get(f"{appiumUrl}/sessions").text

        if content is None or content is "":
            print("No Appium sessions found.")
            return

        print(f"Sessions request content: {content}")

        appiumData = json.loads(content)
        sessionsData = appiumData["value"]
        firstSessionData = sessionsData[0]

        firstSessionId = firstSessionData["id"]
        firstSessionCapabilities = firstSessionData["capabilities"]

        print(f"Session capabilities: {firstSessionCapabilities}")
        print(f"Session ID: {firstSessionId}")

        self.webDriver = self.attach_to_session(appiumUrl, firstSessionId)
        self.set_up_platform_fields(firstSessionCapabilities)
        self.capabilities = firstSessionCapabilities

    def set_up_platform_fields(self, sessionCapabilities):
        # platform is [Android / iOS]
        self.platform = sessionCapabilities["platformName"]
        print(f"Appium platform: {self.platform}")

        self.isAndroidPlatform = self.platform == 'Android'
        self.isIosPlatform = self.platform == 'iOS'

    def attach_to_session(self, executor_url, session_id):
        original_execute = CustomAppiumDriver.execute

        def new_command_execute(self, command, params=None):
            if command == 'newSession':
                return {'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)

        CustomAppiumDriver.execute = new_command_execute
        driver = CustomAppiumDriver(command_executor=executor_url, desired_capabilities={}, direct_connection=False)
        driver.session_id = session_id
        CustomAppiumDriver.execute = original_execute
        return driver
