from typing import List

from pydantic import BaseModel


class BankCard(BaseModel):
    id: str
    sendId: str
    currencyCode: int
    cashbackType: str
    balance: int
    creditLimit: int
    maskedPan: List[str]
    type: str
    iban: str


class AccountSchema(BaseModel):
    clientId: str
    name: str
    webHookUrl: str
    permissions: str
    accounts: List[BankCard]


class Transaction(BaseModel):
    id: str
    time: int
    description: str
    mcc: int
    originalMcc: int
    amount: int
    operationAmount: int
    currencyCode: int
    commissionRate: int
    cashbackAmount: int
    balance: int
    hold: bool
    receiptId: str | None = None
