import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

ROOT_FOLDER = Path(__file__).parent.parent

# GOOGLE PART
GOOGLE_AUTH_FOLDER = ROOT_FOLDER / 'google_auth'
GOOGLE_CREDENTIALS = GOOGLE_AUTH_FOLDER / 'credentials.json'
GOOGLE_USER = GOOGLE_AUTH_FOLDER / 'authorised_user.json'

MONOBANK_REQUEST_ID = os.environ['MONOBANK_REQUEST_ID']
