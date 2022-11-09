from tests.base.appium_base_test import AppiumBaseTest


class TestSignInAccount(AppiumBaseTest):

    def test_enter(self):
        self.signInAccount('b9970@bb.com', 'Qwerty@12345')

    def test_exit(self):
        pass
