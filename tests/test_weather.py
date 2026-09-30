import pytest
from weather import forecast_request, fahrenheit


def test_forecast_request_contains_coordinates():
    request = forecast_request(48.85, 2.35)
    assert request.method == "GET"
    assert "latitude=48.85" in request.url
    assert "longitude=2.35" in request.url
    assert "hourly=temperature_2m" in request.url


@pytest.mark.parametrize("latitude,longitude", [(91, 0), (0, 181)])
def test_invalid_coordinates_rejected(latitude, longitude):
    with pytest.raises(ValueError):
        forecast_request(latitude, longitude)


@pytest.mark.parametrize("celsius,expected", [(0,32), (100,212), (-40,-40)])
def test_temperature_conversion(celsius, expected):
    assert fahrenheit(celsius) == expected
