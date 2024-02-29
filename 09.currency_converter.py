# Currency Converter
def convert_currency(amount, from_currency, to_currency):
    # Replace with actual conversion rates
    conversion_rates = {
        'USD': 1.20,
        'EUR': 1.00,
        'GBP': 0.85,
        'INR': 90.0,  # Example conversion rate for INR
    }

    # Check if both source and target currencies are in the conversion rates dictionary
    if from_currency in conversion_rates and to_currency in conversion_rates:
        # Perform the currency conversion
        converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
        result = round(converted_amount, 2)
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    else:
        # If either the source or target currency is not in the dictionary, return an error message
        print("Invalid currency code")

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
