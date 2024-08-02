import requests
import matplotlib.pyplot as plt

def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def plot_weather_data(data):
    dates = [entry['dt_txt'] for entry in data['list']]
    temperatures = [entry['main']['temp'] for entry in data['list']]

    plt.plot(dates, temperatures, marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather Forecast')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

city = input("Enter city name: ")
api_key = 'd19769ea1e6df01a4ed10964f20475ea'
weather_data = get_weather_data(city, api_key)
plot_weather_data(weather_data)
