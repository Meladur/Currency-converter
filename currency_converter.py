import requests

api_key = "12t1aIq1SMvZvIboHTgtOuFKx0otfzH4"
url = f"https://api.apilayer.com/fixer/convert?to={{to_currency}}&from={{from_currency}}&amount={{amount}}"

headers = {"apikey": api_key}

print("Welcome to the currency converter app ")

from_currency = input("Enter the source currency code (e.g., USD): ").upper()
to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

while True:
    amount = float(input("Please enter your amount (or enter 0 to exit): "))

    if amount == 0:
        print("Exiting the currency converter app. Goodbye!")
        break

    # Construct the URL with the user inputs
    request_url = url.format(to_currency=to_currency, from_currency=from_currency, amount=amount)

    response = requests.get(request_url, headers=headers)

    if response.status_code != 200:
        print("There was an error. Please try again later.")
    else:
        result = response.json()
        converted_amount = result.get("result")
        print(f"Your {amount} from {from_currency} to {to_currency} is {converted_amount:.2f}")
