from unittest.mock import Mock, patch

from src.external_api import convert_currency


def test_convert_currency_rub():
    """Если валюта RUB — не должно быть запроса к API"""
    transaction = {"amount": "100", "currency": {"code": "RUB"}}
    result = convert_currency(transaction)
    assert result == 100.0


def test_convert_currency_usd_with_mock():
    """Тест с моком: конвертация USD -> RUB"""
    transaction = {"amount": "100", "currency": {"code": "USD"}}
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 75.5}}

    with patch("src.external_api.requests.get", return_value=mock_response):
        result = convert_currency(transaction)

    assert result == 7550.0  # 100 * 75.5


def test_convert_currency_eur_with_mock():
    """Тест с моком: конвертация EUR -> RUB"""
    transaction = {"amount": "50", "currency": {"code": "EUR"}}
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 85.0}}

    with patch("src.external_api.requests.get", return_value=mock_response):
        result = convert_currency(transaction)

    assert result == 4250.0  # 50 * 85.0


def test_convert_currency_api_error():
    """Если API недоступен — возвращаем исходную сумму"""
    transaction = {"amount": "100", "currency": {"code": "USD"}}

    with patch("src.external_api.requests.get", side_effect=Exception("API error")):
        result = convert_currency(transaction)

    assert result == 100.0


def test_convert_currency_no_api_key():
    """Если нет API_KEY — возвращаем исходную сумму"""
    transaction = {"amount": "100", "currency": {"code": "USD"}}
    with patch("src.external_api.os.getenv", return_value=None):
        result = convert_currency(transaction)
    assert result == 100.0
