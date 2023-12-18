import requests

def get_conversion_result(api_key, from_currency, to_currency, amount):
    # Construct the API URL with the provided parameters
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
    
    # Set the API key in the headers for authentication
    headers = {"apikey": api_key}

    # Make a GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the response status code is successful (200)
    if response.status_code != 200:
        return None
    else:
        # Parse the JSON response and retrieve the conversion result
        result = response.json()
        return result.get("result")

print("Welcome to the currency converter app ")

# Replace this API key with your actual API key
api_key = "12t1aIq1SMvZvIboHTgtOuFKx0otfzH4"

# Get user input for source and target currencies
from_currency = input("Enter the source currency code (e.g., USD): ").upper()
to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

while True:
    # Get the amount from the user, allowing the user to exit by entering 0
    amount = float(input("Please enter your amount (or enter 0 to exit): "))

    if amount == 0:
        print("Exiting the currency converter app. Goodbye!")
        break

    # Call the function to get the conversion result
    converted_amount = get_conversion_result(api_key, from_currency, to_currency, amount)

    # Check if the conversion was successful
    if converted_amount is not None:
        # Display the result with two decimal places
        print(f"Your {amount} from {from_currency} to {to_currency} is {converted_amount:.2f}")
    else:
        print("There was an error. Please try again later.")
