import requests

# API key and endpoint
api_key = "aa2e690aeee9d78916d00d170bc9ba84"
city = "Yogyakarta"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send a request to the API
response = requests.get(url)
weather_data = response.json()

# Display the weather information
print(f"Temperature in {city}: {weather_data['main']['temp']}K")
