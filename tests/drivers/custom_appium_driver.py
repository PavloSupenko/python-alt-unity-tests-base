import time
from typing import Dict, List, Optional, Union
from appium.options.common.base import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class CustomAppiumDriver(webdriver.Remote):
    def __init__(
            self,
            command_executor: str = 'http://127.0.0.1:4444/wd/hub',
            desired_capabilities: Optional[Dict] = None,
            browser_profile: str = None,
            proxy: str = None,
            keep_alive: bool = True,
            direct_connection: bool = True,
            extensions: Optional[List['WebDriver']] = None,
            strict_ssl: bool = True,
            options: Union[AppiumOptions, List[AppiumOptions]] = None,
    ):
        super().__init__(
            command_executor=command_executor,
            desired_capabilities=desired_capabilities,
            browser_profile=browser_profile,
            proxy=proxy,
            keep_alive=keep_alive,
            direct_connection=direct_connection,
            extensions=extensions,
            strict_ssl=strict_ssl,
            options=options
        )

    def wait_for_element(self, by: str = AppiumBy.ID, value: Union[str, Dict] = None, timeout=20, interval=1):
        timer = 0
        while timer < timeout:
            try:
                element = self.find_element(by=by, value=value)
                return element
            except:
                print(f"Object searching by: {by} with value: {value} not found.")
            finally:
                time.sleep(interval)
                timer += interval

        raise Exception(f"Object searching by: {by} with value: {value} not found and test exited with timeout: {timeout}.")

    def wait_for_element_to_not_be_present(self, by: str = AppiumBy.ID, value: Union[str, Dict] = None, timeout=20, interval=1):
        timer = 0
        while timer < timeout:
            try:
                element = self.find_element(by=by, value=value)
            except:
                return
            finally:
                time.sleep(interval)
                timer += interval

        raise Exception(f"Object searching by: {by} with value: {value} still exist in scene and test exited with timeout: {timeout}.")
