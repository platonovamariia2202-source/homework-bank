import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR."""
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", {}).get("code", "")

    if currency not in ["USD", "EUR"]:
        return amount

    # читаем ключ КАЖДЫЙ РАЗ (чтобы можно было замокать)
    api_key = os.getenv("API_KEY")
    if not api_key:
        return amount

    url = f"http://api.exchangeratesdata.io/v1/latest?apikey={api_key}&base={currency}&symbols=RUB"

    try:
        response = requests.get(url)
        data = response.json()
        rate = data["rates"]["RUB"]
        return float(round(amount * rate, 2))
    except Exception:
        return amount
