import requests

# Weather App
def weather_app():
    # Get user input for the city name
    city = input("Enter the city name: ")

    # Replace with actual OpenWeatherMap API key
    api_key = "c9988ab52aacedc0c0533b4287c2a35d"

    # Construct the URL for the OpenWeatherMap API request
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Make the API request
        response = requests.get(weather_url)
        data = response.json()  # Parse the JSON response

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Extract temperature and weather description from the response
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            # Convert Kelvin to Celsius
            temperature_celsius = round(temperature - 273,2) # Round off to 2 decimal places
            # Print the weather information
            print(f"The current temperature in {city} is {temperature_celsius}°C. Weather: {description}")
        else:
            # Print an error message if the request was not successful
            print(f"Error: {data['message']}")

    except Exception as e:
        # Handle exceptions (e.g., network issues, JSON parsing errors)
        print(f"Error: {e}")

# Run the Weather App
weather_app()
