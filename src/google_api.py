import gspread

from src import config


def get_client():
    return gspread.oauth(credentials_filename=config.GOOGLE_CREDENTIALS, authorized_user_filename=config.GOOGLE_USER)


def get_service():
    return gspread.service_account(filename=config.GOOGLE_SERVICE_ACC)
