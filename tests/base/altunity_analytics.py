import os
import time
from altunityrunner import AltUnityDriver


class AltUnityAnalytics:
    def __init__(self, alt_unity_driver: AltUnityDriver, path: str, class_name: str, assembly: str, method: str):
        self._test_artifacts_path = path
        self._current_analytics_file_number = 0
        self._driver = alt_unity_driver
        self._reader_class_name = class_name
        self._reader_assembly = assembly
        self._method = method

    def save(self, file_name: str):
        self._current_analytics_file_number += 1
        file_path = os.path.join(self._test_artifacts_path, f"{self._current_analytics_file_number}.{file_name}.log")

        # Create subdirectories if it's needed based on filename
        # It's pretty important to pass directory path as the argument, not file path
        screenshot_directory = os.path.dirname(file_path)
        os.makedirs(screenshot_directory, exist_ok=True)
        print(f"Analytics files save directory: {file_path}")

        analytics_data = self.get_analytics_data()

        file = open(file_path, "w")
        save_result = file.write(analytics_data)
        file.close()
        print(f"Saving analytics file on path: {file_path} with result: {save_result}")

    def get_analytics_data(self) -> str:
        analytics_data = self._driver.call_static_method(type_name=self._reader_class_name,
                                                         assembly=self._reader_assembly,
                                                         method_name=self._method,
                                                         type_of_parameters=None,
                                                         parameters=[])

        print(f"Found new analytics events:\n{analytics_data}")
        return analytics_data

    def delay_and_save(self, delay: int, file_name: str):
        time.sleep(delay)
        self.save(file_name=file_name)
