import re
from typing import Any, Dict, List


def search_transactions(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Возвращает транзакции, в описании которых есть искомая строка (регистронезависимо)."""
    if not search_string:
        return []

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = []
    for t in transactions:
        description = t.get("description", "")
        if pattern.search(description):
            result.append(t)
    return result
