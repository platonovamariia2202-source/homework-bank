def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    result_list: list = []
    for item in data_list:
        if item.get("state") == state:
            result_list.append(item)

    return result_list


def sort_by_date(data_list: list, descending: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""

    return sorted(data_list, key=lambda x: x["date"], reverse=descending)
