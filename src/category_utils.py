from collections import Counter
from typing import Any, Dict, List


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по заданным категориям на основе описания."""
    counter = Counter()
    for t in transactions:
        desc = t.get("description", "")
        for cat in categories:
            if cat.lower() in desc.lower():
                counter[cat] += 1
                break  # считаем операцию только в одной категории
    return dict(counter)
