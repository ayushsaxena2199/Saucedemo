from POM.logout import Logout


def test_logout(_driver):
    logout = Logout(_driver)
    logout.enter_email('standard_user')
    logout.enter_pwd('secret_sauce')
    logout.login_btn()
    logout.clk_ham_btn()
    logout.clk_logout()


