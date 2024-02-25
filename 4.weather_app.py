import requests

# Weather App
def weather_app():
    city = input("Enter the city name: ")
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(weather_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"The current temperature in {city} is {temperature}°C. Weather: {description}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error: {e}")

# Run the Weather App
weather_app()
