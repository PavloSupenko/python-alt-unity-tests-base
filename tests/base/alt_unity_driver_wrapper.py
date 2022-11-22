import os
from tests.base.altunity_analytics import AltUnityAnalytics
from tests.drivers.custom_alt_unity_driver import CustomAltUnityDriver


class AltUnityDriverWrapper:

    def __init__(self, test_artifacts_directory: str):
        is_cloud_run = os.environ["IS_CLOUD_RUN"] == 'true'
        alt_unity_port_number = int(os.environ["ALT_UNITY_PORT"])
        self.alt_unity_driver = CustomAltUnityDriver(host="127.0.0.1", enable_logging=True, timeout=30, port=alt_unity_port_number)
        self.analytics = AltUnityAnalytics(alt_unity_driver=self.alt_unity_driver,
                                           path=test_artifacts_directory,
                                           class_name='Bini.Drawing.AnalyticsReader.EventsReader',
                                           assembly='Bini.Drawing.AnalyticsReader',
                                           method='GetLastAnalyticsEvents')

        print(f"Cloud status for test run is: {is_cloud_run}")

    def __del__(self):
        self.alt_unity_driver.stop()

    def save_analytics(self, fileName):
        self.analytics.save(file_name=fileName)

    def get_new_analytics(self):
        return self.analytics.get_analytics_data()
