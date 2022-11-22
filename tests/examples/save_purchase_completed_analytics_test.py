from tests.base.alt_unity_driver_wrapper import AltUnityDriverWrapper


class TestSavePurchaseCompletedAnalytics(AltUnityDriverWrapper):

    def test_enter(self):
        self.save_analytics("purchase_completed")

    def test_exit(self):
        pass
