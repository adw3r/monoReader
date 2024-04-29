import gspread


def test_get_login():
    gc = gspread.oauth(credentials_filename=r'C:\Users\user\Desktop\monoReader\google_secret.json', authorized_user_filename=r'C:\Users\user\Desktop\monoReader\authorised_user.json')
    test_ss = gc.create('test')
    assert test_ss is not None
