import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestParentalGatePass(AltUnityBaseTest):

    def test_enter(self):
        componentName = 'Bini.ToolKit.StandardMenus.ParentalGate.UIView.ParentalGateControllerUni'
        parentalGate = self.altUnityDriver.wait_for_object(By.COMPONENT, value=componentName)

        # Assembly should be defined to not cause 'Not loaded assembly' error
        # Assembly in this case - assembly definition file name
        parentalGate.call_component_method(componentName, 'DoAction', ['true'], None, 'Bini.ToolKit.StandardMenus')
        time.sleep(5)

    def test_exit(self):
        pass
