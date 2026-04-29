import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """Считывает транзакции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """Считывает транзакции из Excel-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []
