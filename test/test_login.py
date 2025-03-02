from POM.login import Login


def test_login(_driver):
    login = Login(_driver)
    login.enter_email('standard_user')
    login.enter_pwd('secret_sauce')
    login.login_btn()

