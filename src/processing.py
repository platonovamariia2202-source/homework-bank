def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ stateсоответствует указанному значению.
    """
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)

    return result


def sort_by_date(data: list, descending: bool = True) -> list:
    """Функция возвращаtт новый список, отсортированный по дате"""

    return sorted(data, key=lambda x: x["date"], reverse=descending)
