import requests

def get_weather(city_name, api_key):
   
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    # If city is found
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]

        print("\n🌦️  Weather Report for:", city_name.title())
        print("--------------------------------------")
        print(f"🌡️  Temperature: {main['temp']}°C")
        print(f"🤒  Feels Like: {main['feels_like']}°C")
        print(f"💧  Humidity: {main['humidity']}%")
        print(f"🌬️  Pressure: {main['pressure']} hPa")
        print(f"☁️  Weather: {weather['main']} - {weather['description'].title()}")
        print("--------------------------------------")

    else:
        print("\nCity Not Found! Please check the name.")



print("=== 🌍 Simple Weather App ===")
api_key = input("Enter your OpenWeatherMap API Key: ").strip()
city = input("Enter city name: ").strip()

get_weather(city, api_key)
