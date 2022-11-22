import time
from unittest import TestCase
from alttester import By
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestParentalGatePass(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(True)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        componentName = 'Bini.ToolKit.StandardMenus.ParentalGate.UIView.ParentalGateControllerUni'
        parentalGate = self.alt_unity_driver.wait_for_object(By.COMPONENT, value=componentName)

        # Assembly should be defined to not cause 'Not loaded assembly' error
        # Assembly in this case - assembly definition file name
        parentalGate.call_component_method(componentName, 'DoAction', ['true'], None, 'Bini.ToolKit.StandardMenus')

        time.sleep(2)
        self.save_analytics("parental_gate_pass")

    def test_exit(self):
        pass
