from unittest import TestCase
from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper
from tests.base.subscription_type import SubscriptionType


class TestDiscardLastSubscription(TestCase, AltUnityDriverWrapper):

    def setUp(self):
        super().set_up(False)

    def tearDown(self):
        super().tear_down()

    def test_enter(self):
        self.discardLastSubscription()
        self.waitSubscription(subscription_type=SubscriptionType.Month)

    def test_exit(self):
        pass
