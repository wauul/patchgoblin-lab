import requests


def forecast_request(latitude, longitude):
    if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
        raise ValueError("Coordinates out of range")
    return requests.Request("GET", "https://api.open-meteo.com/v1/forecast", params={"latitude": latitude, "longitude": longitude, "hourly": "temperature_2m"}).prepare()


def fahrenheit(celsius):
    return celsius * 9 / 5 + 32
