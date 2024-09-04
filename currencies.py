import requests
from decimal import Decimal

JPY_RUB = 0.63

ERROR_CURRENCY_FROM_NOT_FOUND = -1
ERROR_CURRENCY_TO_NOT_FOUND = -2
ERROR_FETCHING_VALUE = -3

CURRENCY_API_BASE_URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency}.json'
CURRENCIES_LIST_API_URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
ALL_CURRENCIES_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.min.json"

default_currency_key = "default_currency"

FAVOURITE_CURRENCIES = [
    'EUR',
    'USD',
    'GBP',
]

DEFAULT_LOCAL_CURRENCY = 'UAH'

def get_currencies_ratios(
        from_currency: str,
        to_currencies: list[str]
):
    from_currency = from_currency.lower()

    url = CURRENCY_API_BASE_URL.format(currency=from_currency)
    response = requests.get(url)

    json_data = response.json()
    values = json_data[from_currency]

    result = []
    for currency in to_currencies:
        to_currency = currency.lower()
        if to_currency in values:
            result.append(values[to_currency])
        else:
            result.append(0)

    return result

def fetch_available_currencies():
    response = requests.get(ALL_CURRENCIES_URL)
    if response.status_code != 200:
        return {}
    return response.json()


def is_currency_available(currency: str) -> bool:
    return currency.lower() in fetch_available_currencies()



def get_correct_currencies(currency: str, default_to: str = "RUB"):
    if " " in currency:
        currency_from, _, currency_to = currency.partition(" ")
        currency_from = currency_from.strip()
        currency_to = currency_to.strip()
    else:
        currency_from = currency
        currency_to = default_to

    return currency_from, currency_to

def get_currency_ratio(currency_from, currency_to):
    currency_from = currency_from.lower()
    currency_to = currency_to.lower()

    url = CURRENCY_API_BASE_URL.format(currency=currency_from)
    response = requests.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            return ERROR_CURRENCY_FROM_NOT_FOUND
        return ERROR_FETCHING_VALUE

    json_data = response.json(parse_float=Decimal)

    if json_data[currency_from].get(currency_to):
        return json_data[currency_from][currency_to]
    else:
        return ERROR_CURRENCY_TO_NOT_FOUND