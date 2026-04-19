from typing import Any, Dict, Generator, Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[Dict[str, Any]]:
    """Генератор, возвращающий транзакции с заданной валютой."""

    for transaction in transactions:
        try:
            trans_currency = transaction["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError):
            continue
        if trans_currency == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Генератор, возвращающий описание каждой транзакции."""

    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номеров карт в заданном диапазоне."""

    for number in range(start, end + 1):
        num_str = str(number).zfill(16)
        formatted = " ".join([num_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted
