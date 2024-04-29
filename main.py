from datetime import datetime, timedelta

import gspread_dataframe
import httpx
import pandas

from src import config, schemas, parsers, google_api


def reformat_columns(df: pandas.DataFrame):
    return df[[
        'id',
        'reformatted time',
        'description',
        'reformatted amount',
        'time',
        'mcc',
        'originalMcc',
        'amount',
        'operationAmount',
        'currencyCode',
        'commissionRate',
        'cashbackAmount',
        'balance',
        'hold',
        'receiptId',
        'card_type'
    ]]


def main() -> None:
    account_info: httpx.Response = parsers.MonoApi.get_account_info()
    account_info_schema: schemas.AccountSchema = schemas.AccountSchema(**account_info.json())
    cards: list[schemas.BankCard] = [
        acc for acc in account_info_schema.accounts if
        acc.balance > 0 and acc.currencyCode == 980
    ]
    now: datetime = datetime.now()
    start_of_the_month: datetime = now - timedelta(days=31)
    now_in_timestamp: int = round(datetime.timestamp(now))
    start_of_the_month_in_timestamp: int = round(datetime.timestamp(start_of_the_month))

    frames = pandas.DataFrame()
    for card in cards:
        get_card_info: httpx.Response = parsers.MonoApi.get_card_info(
            card.id, start_of_the_month_in_timestamp, now_in_timestamp
        )
        df = pandas.DataFrame([schemas.Transaction(**t).dict() for t in get_card_info.json()])
        df['card_type'] = card.type
        frames = pandas.concat([frames, df])

    frames['reformatted amount'] = [i / 100 for i in frames['amount']]
    frames['reformatted time'] = [datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y') for timestamp in
                                  frames['time']]
    frames = reformat_columns(frames)
    frames = frames.sort_values('time')
    gc = google_api.get_client()
    ws = gc.open_by_url(config.URL_TO_MAIN).worksheet('data')
    gspread_dataframe.set_with_dataframe(ws, frames, allow_formulas=False)


if __name__ == '__main__':
    main()
