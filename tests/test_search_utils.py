from src.search_utils import search_transactions


def test_search_transactions_found():
    data = [{"description": "Перевод организации"}, {"description": "Оплата услуг"}]
    result = search_transactions(data, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_search_transactions_not_found():
    data = [{"description": "Перевод организации"}]
    result = search_transactions(data, "подарок")
    assert result == []


def test_search_transactions_empty_list():
    result = search_transactions([], "что-то")
    assert result == []


def test_search_transactions_case_insensitive():
    data = [{"description": "Перевод Организации"}]
    result = search_transactions(data, "организации")
    assert len(result) == 1
