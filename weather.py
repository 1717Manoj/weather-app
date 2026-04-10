import requests

API_KEY = "047c61cf7aa0b048243b8906c6aa049c"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print("\nDEBUG DATA:", data)  # 👈 IMPORTANT (to see actual error)

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\n🌤️ Weather Details:")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")

    else:
        print("❌ Error:", data.get("message", "Something went wrong"))

while True:
    city = input("\nEnter city name (or 'exit'): ")

    if city.lower() == "exit":
        break

    get_weather(city)
    