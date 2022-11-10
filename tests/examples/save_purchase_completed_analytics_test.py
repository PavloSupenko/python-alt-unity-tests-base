from tests.base.altunity_base_test import AltUnityBaseTest


class TestSavePurchaseCompletedAnalytics(AltUnityBaseTest):

    def test_enter(self):
        self.saveAnalytics("purchase_completed")

    def test_exit(self):
        pass
