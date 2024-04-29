import gspread

import config


def get_client():
    return gspread.oauth(credentials_filename=config.GOOGLE_CREDENTIALS, authorized_user_filename=config.GOOGLE_USER)
