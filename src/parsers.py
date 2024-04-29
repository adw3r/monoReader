import httpx

from src import config


class MonoApi:

    @staticmethod
    def get_card_info(card_id: str | int, time_from: str | int, time_to: str | int) -> httpx.Response:
        headers = {
            'accept': 'application/json',
            'x-request-id': config.MONOBANK_REQUEST_ID,
        }

        response = httpx.get(
            f'https://api.mono.sominemo.com/request/personal/statement/{card_id}/{time_from}/{time_to}',
            headers=headers,
        )
        return response

    @staticmethod
    def get_account_info() -> httpx.Response:
        headers = {
            'accept': 'application/json',
            'x-request-id': config.MONOBANK_REQUEST_ID,
        }

        response = httpx.get('https://api.mono.sominemo.com/request/personal/client-info', headers=headers)
        return response
