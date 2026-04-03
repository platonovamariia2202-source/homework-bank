def filter_by_currency(transactions: list, currency_code: str):
    """Генератор, возвращающий транзакции с заданной валютой."""

    for transaction in transactions:
        try:
            trans_currency = transaction["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError):
            continue
        if trans_currency == currency_code:
            yield transaction
