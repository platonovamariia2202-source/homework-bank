import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 3, "description": "Перевод с карты на карту", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 4, "description": "Перевод организации", "operationAmount": {"currency": {"code": "EUR"}}},
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    assert next(usd_gen)["id"] == 1
    assert next(usd_gen)["id"] == 3


def test_filter_by_currency_not_found(sample_transactions):
    gbp_gen = filter_by_currency(sample_transactions, "GBP")
    with pytest.raises(StopIteration):
        next(gbp_gen)


def test_filter_by_currency_empty_list():
    empty_gen = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_gen)


def test_filter_by_currency_missing_key():
    """Транзакция без ключа operationAmount должна пропускаться."""
    transactions = [{"id": 1, "description": "Без валюты"}]
    gen = filter_by_currency(transactions, "USD")
    with pytest.raises(StopIteration):
        next(gen)


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


def test_card_number_generator_range():
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"


def test_card_number_generator_single():
    gen = card_number_generator(10, 10)
    assert next(gen) == "0000 0000 0000 0010"


def test_card_number_generator_format():
    gen = card_number_generator(123, 123)
    assert next(gen) == "0000 0000 0000 0123"
