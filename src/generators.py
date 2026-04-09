def filter_by_currency(transactions: list, currency_code: str):
    """Генератор, возвращающий транзакции с заданной валютой."""

    for transaction in transactions:
        try:
            trans_currency = transaction["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError):
            continue
        if trans_currency == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, возвращающий описание каждой транзакции."""

    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")
