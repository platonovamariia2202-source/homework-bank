import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "USD"}}
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"currency": {"code": "RUB"}}
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"currency": {"code": "USD"}}
        },
        {
            "id": 4,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "EUR"}}
        }
    ]


@pytest.mark.parametrize("currency, first_id, second_id", [
    ("USD", 1, 3),
    ("RUB", 2, None),
    ("EUR", 4, None),
])
def test_filter_by_currency(sample_transactions, currency, first_id, second_id):
    gen = filter_by_currency(sample_transactions, currency)
    assert next(gen)["id"] == first_id
    if second_id is not None:
        assert next(gen)["id"] == second_id
    else:
        with pytest.raises(StopIteration):
            next(gen)


@pytest.mark.parametrize("currency", ["USD", "GBP"])
def test_filter_by_currency_empty(currency):
    empty_gen = filter_by_currency([], currency)
    with pytest.raises(StopIteration):
        next(empty_gen)


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    assert next(desc_gen) == "Перевод организации"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод с карты на карту"
    assert next(desc_gen) == "Перевод организации"


def test_transaction_descriptions_empty():
    empty_gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_gen)


@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 10, ["0000 0000 0000 0010"]),
])
def test_card_number_generator(start, end, expected):
    gen = card_number_generator(start, end)
    for value in expected:
        assert next(gen) == value
    with pytest.raises(StopIteration):
        next(gen)
