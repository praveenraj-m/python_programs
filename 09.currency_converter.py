import requests

# Currency Converter with API
def convert_currency(amount, from_currency, to_currency):
    # API URL for fetching exchange rates
    api_url = "https://v6.exchangerate-api.com/v6/79c4fa1306937cdc8e97ba63/latest/USD"

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        data = response.json()

        # Check if the API request was successful
        if response.status_code == 200 and data["result"] == "success":
            # Get conversion rates from the API response
            conversion_rates = data["conversion_rates"]

            # Check if both source and target currencies are in the conversion rates
            if from_currency in conversion_rates and to_currency in conversion_rates:
                # Perform the currency conversion
                converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
                result = round(converted_amount, 2)
                print(f"{amount} {from_currency} is equal to {result} {to_currency}")
            else:
                # If either the source or target currency is not in the API response, return an error message
                print("Invalid currency code")
        else:
            # If the API request fails or the response indicates an error, print an error message
            print(f"Error: {data.get('error', 'Unknown error')}")

    except Exception as e:
        # Handle other exceptions (e.g., network issues)
        print(f"Error: {e}")

# Example usage with user prompts
while True:
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
        continue  # Restart the loop to get a valid input

    print("Please type the currency code listed correctly \n'USD'\n'EUR',\n'GBP'\n'INR' ")
   
    from_currency = input("Enter the from currency: ").upper()
    to_currency = input("Enter the to currency: ").upper()
    convert_currency(amount, from_currency, to_currency)

    # Ask if the user wants to perform another conversion
    another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
    if another_conversion != 'yes':
        break
