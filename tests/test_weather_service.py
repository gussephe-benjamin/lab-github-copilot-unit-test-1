import pytest
from unittest.mock import Mock, patch
from weather_service import get_weather


class TestGetWeather:
    """Tests for get_weather function using mocks."""

    @patch('weather_service.requests.get')
    def test_get_weather_success(self, mock_get):
        """Test successful weather API call with dummy data."""
        # Arrange: Configure mock with dummy weather data
        dummy_weather_data = {
            "location": "Lima",
            "temperature": 25.5,
            "humidity": 65,
            "condition": "Sunny",
            "wind_speed": 12.3,
            "forecast": [
                {"day": "Monday", "temp": 26.0},
                {"day": "Tuesday", "temp": 24.5}
            ]
        }
        
        mock_response = Mock()
        mock_response.json.return_value = dummy_weather_data
        mock_get.return_value = mock_response

        # Act
        result = get_weather("Lima")

        # Assert
        assert result == dummy_weather_data
        assert result["location"] == "Lima"
        assert result["temperature"] == 25.5
        assert result["condition"] == "Sunny"
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/Lima")

    @patch('weather_service.requests.get')
    def test_get_weather_different_location(self, mock_get):
        """Test weather API with different location."""
        # Arrange
        dummy_data = {
            "location": "New York",
            "temperature": 15.0,
            "humidity": 80,
            "condition": "Cloudy"
        }
        
        mock_response = Mock()
        mock_response.json.return_value = dummy_data
        mock_get.return_value = mock_response

        # Act
        result = get_weather("New York")

        # Assert
        assert result["location"] == "New York"
        assert result["temperature"] == 15.0
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/New York")

    @patch('weather_service.requests.get')
    def test_get_weather_empty_response(self, mock_get):
        """Test weather API with empty response."""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        # Act
        result = get_weather("UnknownCity")

        # Assert
        assert result == {}

    @patch('weather_service.requests.get')
    def test_get_weather_rainy_conditions(self, mock_get):
        """Test weather API with rainy weather dummy data."""
        # Arrange
        rainy_data = {
            "location": "London",
            "temperature": 12.0,
            "humidity": 90,
            "condition": "Rainy",
            "precipitation": 5.5,
            "wind_speed": 8.0
        }
        
        mock_response = Mock()
        mock_response.json.return_value = rainy_data
        mock_get.return_value = mock_response

        # Act
        result = get_weather("London")

        # Assert
        assert result["condition"] == "Rainy"
        assert result["precipitation"] == 5.5
        assert result["humidity"] == 90

    @patch('weather_service.requests.get')
    def test_get_weather_api_called_with_correct_url(self, mock_get):
        """Verify API is called with the correct URL format."""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {"location": "Test"}
        mock_get.return_value = mock_response

        # Act
        get_weather("Santiago")

        # Assert
        expected_url = "https://api.weather.com/v3/weather/Santiago"
        mock_get.assert_called_once_with(expected_url)
