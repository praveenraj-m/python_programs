# Currency Converter
def convert_currency(amount, from_currency, to_currency):
    # Replace with actual conversion rates
    conversion_rates = {
        'USD': 1.20,
        'EUR': 1.00,
        'GBP': 0.85,
        'INR': 90.0,  # Example conversion rate for INR
    }

    if from_currency in conversion_rates and to_currency in conversion_rates:
        converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
        return round(converted_amount, 2)
    else:
        return "Invalid currency code"

# Example usage
amount = 100
from_currency = 'USD'
to_currency = 'INR'

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
