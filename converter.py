import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert(amount, from_currency, to_currency):
    response = requests.get(API_URL)
    rates = response.json()["rates"]
    if from_currency != "USD":
        amount = amount / rates[from_currency]
    return round(amount * rates[to_currency], 2)

if __name__ == "__main__":
    from_currency = input("З якої валюти (USD, EUR, UAH)?: ").upper()
    to_currency = input("У яку валюту (USD, EUR, UAH)?: ").upper()
    amount = float(input("Сума: "))
    print(f"Конвертована сума: {convert(amount, from_currency, to_currency)} {to_currency}")
