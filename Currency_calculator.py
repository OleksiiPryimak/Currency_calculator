# python (location)/Currency_calculator.py USD 2023.03.10
# python (location)/Currency_calculator.py USD
# 2021 sep 6
# python (location)/Currency_calculator.py
# usd
# 6 sep 2021

import sys

from dateutil import parser
import requests

print("Currency calculator")

try:
    currency = sys.argv[1]
except IndexError:
    currency = input("Enter the currency: ")
currency = currency.upper()

try:
    date_as_str = sys.argv[2]
except IndexError:
    date_as_str = input("Give the date: ")

try:
    date = parser.parse(date_as_str)
except ValueError:
    print("Invalid date format")
    sys.exit(1)

date_for_url = date.strftime('%Y-%m-%d')

url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_for_url}?format=json"
response = requests.get(url)
if response.status_code == 404:
    print ("No data")
    sys.exit(3)

json = response.json()
try:
    rate = json['rates'][0]['mid']
except (ValueError, KeyError):
    print('invalid server responce')
    sys.exit(4)

print(f"1 {currency} = {rate} PLN on {date.day}/{date.month}/{date.year}")