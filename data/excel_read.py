import xlrd

path = r'D:\POM Frameworks\Practice 23\data\locator.xlsx'

locator_workbook = xlrd.open_workbook(path)

# login
login_worksheet = locator_workbook.sheet_by_name('login Page')
login_rows = login_worksheet.get_rows()
login_header = next(login_rows)


def login_locator():
    login_dict = {}
    for i in login_rows:
        login_dict[i[0].value] = (i[1].value, i[2].value)
    return login_dict


# logout
logout_worksheet = locator_workbook.sheet_by_name('Logout')
logout_rows = logout_worksheet.get_rows()
logout_header = next(logout_rows)


def logout_locator():
    logout_dict = {}
    for i in logout_rows:
        logout_dict[i[0].value] = (i[1].value, i[2].value)
    return logout_dict







