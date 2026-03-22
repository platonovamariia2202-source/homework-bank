import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03"},
        {"id": 4, "state": "CANCELED", "date": "2024-01-04"},
    ]


def test_filter_by_state_default(sample_data):
    """Тест: фильтрация по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(sample_data):
    """Тест: фильтрация по CANCELED"""
    result = filter_by_state(sample_data, "CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_filter_by_state_empty():
    """Тест: пустой список"""
    result = filter_by_state([])
    assert result == []


def test_sort_by_date_default(sample_data):
    """Тест: сортировка по умолчанию (убывание)"""
    result = sort_by_date(sample_data)
    dates = [item["date"] for item in result]
    assert dates == ["2024-01-04", "2024-01-03", "2024-01-02", "2024-01-01"]


def test_sort_by_date_ascending(sample_data):
    """Тест: сортировка по возрастанию"""
    result = sort_by_date(sample_data, descending=False)
    dates = [item["date"] for item in result]
    assert dates == ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"]