from tests.base.appium_base_test import AppiumBaseTest
from tests.base.subscription_type import SubscriptionType


class TestDiscardLastSubscription(AppiumBaseTest):

    def test_enter(self):
        self.discardLastSubscription()
        self.waitSubscription(subscription_type=SubscriptionType.Month)

    def test_exit(self):
        pass
