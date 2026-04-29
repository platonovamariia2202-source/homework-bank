from unittest.mock import patch, Mock
from src.file_processing import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv_success():
    """Успешное чтение CSV через mock"""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]

    with patch("pandas.read_csv", return_value=mock_df):
        result = read_transactions_from_csv("dummy.csv")

    assert result == [{"id": 1, "amount": 100}]


def test_read_transactions_from_csv_error():
    """Ошибка при чтении CSV — возвращаем пустой список"""
    with patch("pandas.read_csv", side_effect=Exception("File error")):
        result = read_transactions_from_csv("bad.csv")

    assert result == []


def test_read_transactions_from_excel_success():
    """Успешное чтение Excel через mock"""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_transactions_from_excel("dummy.xlsx")

    assert result == [{"id": 2, "amount": 200}]


def test_read_transactions_from_excel_error():
    """Ошибка при чтении Excel — возвращаем пустой список"""
    with patch("pandas.read_excel", side_effect=Exception("File error")):
        result = read_transactions_from_excel("bad.xlsx")

    assert result == []
