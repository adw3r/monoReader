from pathlib import Path


ROOT_FOLDER = Path(__file__).parent.parent

# GOOGLE PART
GOOGLE_AUTH_FOLDER = ROOT_FOLDER / 'google_auth'
GOOGLE_CREDENTIALS = GOOGLE_AUTH_FOLDER / 'credentials.json'
GOOGLE_USER = GOOGLE_AUTH_FOLDER / 'authorised_user.json'


MONOBANK_REQUEST_ID = 'b4b90e5bae8f1e8a0e1c12798bd75b28e88b44f3'
