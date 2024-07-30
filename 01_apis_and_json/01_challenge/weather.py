# ここにコードを書いてください
import requests
import sys

API_KEY = '109ff95d973ee97bddd07bc2f6aec95f'

def search_city(city_name):
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching the city data.")
        return None

    city_data = response.json()
    if not city_data:
        return None

    return city_data


def weather_forecast(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching the weather data.")
        return None
    
    forecast_data = response.json()
    daily_forecasts = []
    for i in range(0, len(forecast_data['list']), 8): # 3時間毎のデータなので、8つごとに1日のデータがある
        weather = forecast_data['list'][i]
        date = weather['dt_txt'].split(' ')[0]
        temp = weather['main']['temp_max']
        condition = weather['weather'][0]['description']
        daily_forecasts.append({'date': date, 'temp': temp, 'condition': condition})

    return daily_forecasts


def main():
    while True:
        try:
            city = input("City?\n> ")
            city_data = search_city(city)
            if city_data is None:
                print("City not found. Please try again.")
                continue

            if len(city_data) > 1:
                print("Multiple matches found, which city did you mean?")
                for i, option in enumerate(city_data, 1):
                    print(f"{i}. {option['name']},{option['country']}")
                choice = int(input("> ")) - 1
                if choice < 0 or choice >= len(city_data):
                    print("Invalid choice, please try again.")
                    continue
            else:
                choice = 0
        
            selected_city = city_data[choice]
            forecast = weather_forecast(selected_city['lat'], selected_city['lon'])
            if forecast is None:
                print("Could not fetch weather forecast. Please try again.")
                continue

            print(f"Here's the weather in {selected_city['name']}")
            for day in forecast:
                print(f"{day['date']}: {day['condition']} ({day['temp']}°C)")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            sys.exit()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()