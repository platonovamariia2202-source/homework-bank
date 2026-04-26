import json

from src.utils import get_transactions_from_json


def test_get_transactions_success(tmp_path):
    """Успешное чтение JSON-файла со списком"""
    test_data = [{"id": 1}, {"id": 2}]
    file_path = tmp_path / "test.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    result = get_transactions_from_json(str(file_path))
    assert result == test_data


def test_get_transactions_empty_list(tmp_path):
    """Пустой список в JSON"""
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([], f)

    result = get_transactions_from_json(str(file_path))
    assert result == []


def test_get_transactions_not_list(tmp_path):
    """Если JSON содержит не список — возвращаем пустой список"""
    file_path = tmp_path / "not_list.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"key": "value"}, f)

    result = get_transactions_from_json(str(file_path))
    assert result == []


def test_get_transactions_file_not_found():
    """Файл не найден"""
    result = get_transactions_from_json("nonexistent.json")
    assert result == []


def test_get_transactions_invalid_json(tmp_path):
    """Некорректный JSON"""
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("not a json")

    result = get_transactions_from_json(str(file_path))
    assert result == []
