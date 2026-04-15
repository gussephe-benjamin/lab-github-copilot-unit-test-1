from unittest.mock import patch, Mock
from weather_service import get_weather

def test_get_weather_with_mock():
    dummy_data = {"temp": 25, "condition": "Sunny"}

    mock_response = Mock()
    mock_response.json.return_value = dummy_data

    with patch("weather_service.requests.get", return_value=mock_response) as mock_get:
        result = get_weather("lima")

        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/lima")
        assert result == dummy_data