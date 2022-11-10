import time
from typing import List
from altunityrunner import AltUnityDriver, By


class CustomAltUnityDriver(AltUnityDriver):
    def __init__(self, host="127.0.0.1", port=13000, enable_logging=False, timeout=None,
                 markersComponent='Bini.Drawing.Markers.FeatureMarker', markersAssembly='Bini.Drawing.Markers'):
        super().__init__(host, port, enable_logging, timeout)
        self.componentName = markersComponent
        self.assemblyName = markersAssembly

    def wait_for_object_with_marker(self, target_marker: str, camera_by=By.NAME, camera_value="", timeout=20, interval=0.5, enabled=True):
        timer = 0
        while timer < timeout:
            try:
                markedObject = self.find_object_with_marker(target_marker=target_marker, camera_by=camera_by, camera_value=camera_value, enabled=enabled)
                return markedObject
            except:
                print(f"Object with marker: {target_marker} not found.")
            finally:
                time.sleep(interval)
                timer += interval

        raise Exception(f"Object with marker: {target_marker} not found and test exited with timeout: {timeout}.")

    def wait_for_object_with_any_marker(self, target_markers: List[str], camera_by=By.NAME, camera_value="", timeout=20, interval=0.5, enabled=True):
        timer = 0
        while timer < timeout:
            try:
                markedObject = self.find_object_with_any_marker(target_markers=target_markers, camera_by=camera_by, camera_value=camera_value, enabled=enabled)
                return markedObject
            except:
                print(f"Object with any marker of: {target_markers} not found.")
            finally:
                time.sleep(interval)
                timer += interval

        raise Exception(f"Object with any marker of: {target_markers} not found and test exited with timeout: {timeout}.")

    def wait_for_object_with_marker_to_not_be_present(self, target_marker: str, camera_by=By.NAME, camera_value="", timeout=20, interval=0.5, enabled=True):
        timer = 0
        while timer < timeout:
            try:
                markedObject = self.find_object_with_marker(target_marker=target_marker, camera_by=camera_by, camera_value=camera_value, enabled=enabled)
            except:
                return
            finally:
                time.sleep(interval)
                timer += interval

        raise Exception(f"Object with marker: {target_marker} still exist in scene and test exited with timeout: {timeout}.")

    def find_object_with_marker(self, target_marker: str, camera_by=By.NAME, camera_value="", enabled=True):
        markedObjects = self.find_objects_with_marker(camera_by=camera_by, camera_value=camera_value, enabled=enabled)
        print(f"Found {len(markedObjects)} marked objects in scene")

        for markedObject in markedObjects:
            print(f"Checking object: {markedObject.name}")
            marker = markedObject.call_component_method(component_name=self.componentName, method_name='GetMarker',
                                                        parameters=[], type_of_parameters=None, assembly=self.assemblyName)
            print(f"Marked object with value: {marker} found.")
            if marker == target_marker:
                return markedObject

        raise Exception(f"Object with marker: {target_marker} not found.")

    def find_object_with_any_marker(self, target_markers: List[str], camera_by=By.NAME, camera_value="", enabled=True):
        markedObjects = self.find_objects_with_marker(camera_by=camera_by, camera_value=camera_value, enabled=enabled)
        print(f"Found {len(markedObjects)} marked objects in scene")

        for markedObject in markedObjects:
            print(f"Checking object: {markedObject.name}")
            marker = markedObject.call_component_method(component_name=self.componentName, method_name='GetMarker',
                                                        parameters=[], type_of_parameters=None, assembly=self.assemblyName)
            print(f"Marked object with value: {marker} found.")
            for target_marker in target_markers:
                if marker == target_marker:
                    return markedObject

        raise Exception(f"Object with any marker of: {target_markers} not found.")

    def find_objects_with_marker(self, camera_by=By.NAME, camera_value="", enabled=True):
        markedObjects = self.find_objects(By.COMPONENT, value=self.componentName, camera_by=camera_by, camera_value=camera_value, enabled=enabled)
        return markedObjects
