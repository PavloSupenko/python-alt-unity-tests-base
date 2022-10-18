import os
import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestQuestionnaireSkip(AltUnityBaseTest):

    def test_enter(self):
        print("Finding skip survey button")
        skipButton = self.altUnityDriver.wait_for_object_with_marker('Survey/Skip')

        print("Tap skip survey button")
        skipButton.tap()

        self.saveScreenshot(os.path.join("Survey", "enter"))

        time.sleep(2)

    def test_exit(self):
        print("Finding skip survey button again")
        self.altUnityDriver.wait_for_object_with_marker_to_not_be_present('Survey/Skip')
        self.saveScreenshot(os.path.join("Survey", "exit"))
