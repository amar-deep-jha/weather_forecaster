import requests

def get_weather(city):
    try:
        api_key = "75f76f7c836c02a5ad8cb9193a2789cc"  # 🔴 Replace this with your actual key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # 🔍 Debugging: check if API returned error
        if data.get("cod") != 200:
            return f"⚠️ API Error: {data.get('message', 'Unknown error')}"

        # Extract weather info
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        return f"🌍 {city_name}, {country}\n🌡️ Temp: {temp}°C\n☁️ Weather: {weather}"

    except requests.exceptions.RequestException as e:
        return f"⚠️ Network/Request error: {e}"
    except KeyError:
        return "⚠️ Unexpected data format."
    finally:
        print("Request completed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
