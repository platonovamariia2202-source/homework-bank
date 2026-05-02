from src.category_utils import count_operations_by_category


def test_count_operations_by_category():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
    ]
    categories = ["Перевод организации", "Оплата услуг"]
    result = count_operations_by_category(data, categories)
    assert result == {"Перевод организации": 2, "Оплата услуг": 1}


def test_count_operations_no_match():
    data = [{"description": "Перевод"}]
    categories = ["Покупка"]
    result = count_operations_by_category(data, categories)
    assert result == {}
