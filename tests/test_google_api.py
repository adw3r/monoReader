from src import google_api


def test_get_login():
    gc = google_api.get_client()
    assert gc is not None
