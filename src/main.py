from typing import Any, Dict, List

from external_api import convert_currency
from file_processing import read_transactions_from_csv, read_transactions_from_excel
from processing import filter_by_state, sort_by_date
from search_utils import search_transactions
from utils import get_transactions_from_json


def load_transactions(source: int) -> List[Dict[str, Any]]:
    """Загружает транзакции из выбранного источника."""
    if source == 1:
        return get_transactions_from_json("data/operations.json")
    elif source == 2:
        return read_transactions_from_csv("data/transactions.csv")
    elif source == 3:
        return read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        return []


def get_valid_status() -> str:
    """Запрашивает у пользователя статус, пока не будет введён корректный."""
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()
        if status in valid_statuses:
            return status
        else:
            print(f'Статус операции "{status}" недоступен.')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = int(input().strip())
    transactions = load_transactions(choice)

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    # Фильтрация по статусу
    status = get_valid_status()
    filtered = filter_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice in ["да", "yes", "y"]:
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        descending = order != "по возрастанию"
        filtered = sort_by_date(filtered, descending)

    # Только рублевые транзакции
    rub_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_choice in ["да", "yes", "y"]:
        rub_filtered = []
        for t in filtered:
            currency = t.get("operationAmount", {}).get("currency", {}).get("code", "")
            if currency == "RUB":
                rub_filtered.append(t)
        filtered = rub_filtered

    # Поиск по описанию
    search_prompt = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    search_choice = input(search_prompt).strip().lower()
    if search_choice in ["да", "yes", "y"]:
        search_word = input("Введите слово для поиска:\n").strip()
        filtered = search_transactions(filtered, search_word)

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered)}")

    for t in filtered:
        date = t.get("date", "")[:10].replace("-", ".")
        desc = t.get("description", "")
        from_acc = t.get("from", "")
        to_acc = t.get("to", "")
        amount = t.get("operationAmount", {}).get("amount", "0")
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "")
        converted = convert_currency(t) if currency in ["USD", "EUR"] else float(amount)

        print(f"\n{date} {desc}")
        if from_acc and to_acc:
            print(f"{from_acc} -> {to_acc}")
        print(f"Сумма: {converted} {currency if currency in ['RUB', 'USD', 'EUR'] else 'RUB'}")


if __name__ == "__main__":
    main()
