import json
from typing import Any, Dict, List


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
