import sys
import urllib.request
import json
from urllib.error import URLError


def fetch_json(url, headers):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode("utf-8")
            return json.loads(response_data)
    except URLError as e:
        print(f"Error fetching data: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e.msg}")
    return None


user_agent = "python-weather-gov|tyler"
headers = {"User-Agent": user_agent}

latitude = 39.5
longitude = -85.7
grid_points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
grid_data = fetch_json(grid_points_url, headers)

if grid_data:
    forecast_url = grid_data['properties']['forecastHourly']
    forecast_data = fetch_json(forecast_url, headers)

    if forecast_data:
        periods = forecast_data['properties']['periods']
        for period in periods:
            print(f"Time: {period['startTime']}, Temperature: {period['temperature']} {period['temperatureUnit']}, "
                  f"Forecast: {period['shortForecast']}")
