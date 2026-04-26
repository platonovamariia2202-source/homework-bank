# Банковское приложение

## Описание
Проект для обработки банковских операций.

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/platonovamariia2202-source/homework-bank.git

text

2. Установите зависимости:
poetry install

text

## Использование

1. Маскирует номер карты и счетов.
2. Фильтрует операции по статусу.
3. Сортирует операции по дате.

## Тестирование

В проекте используется **pytest** для модульного тестирования.

### Запуск всех тестов:

```bash
pytest tests/
```

### Запуск с отчётом о покрытии:

```bash
pytest --cov=src tests/
```

### Генерация HTML-отчёта о покрытии:

```bash
pytest --cov=src --cov-report=html tests/
```

## Генераторы для обработки транзакций

Модуль `generators` содержит три генератора:

### `filter_by_currency(transactions, currency_code)`
Возвращает транзакции с заданной валютой.

Пример:
```python
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

### `transaction_descriptions(transactions)`
Возвращает описания транзакций по очереди.

Пример:
```python
descriptions = transaction_descriptions(transactions)
print(next(descriptions))  # "Перевод организации"
```

### `card_number_generator(start, end)`
Генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

Пример:
```python
for card in card_number_generator(1, 5):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005
```

## Обработка JSON-данных

Модуль `utils` содержит функцию `get_transactions_from_json`, которая загружает список транзакций из JSON-файла.

**Пример использования:**
```python
from src.utils import get_transactions_from_json

transactions = get_transactions_from_json("data/operations.json")
```

## Конвертация валют

Модуль `external_api` содержит функцию `convert_currency`, которая конвертирует сумму в USD или EUR в рубли через внешнее API.

**Пример:**
```python
from src.external_api import convert_currency

transaction = {"amount": "100", "currency": {"code": "USD"}}
rub_amount = convert_currency(transaction)
```

markdown
## Переменные окружения

Для работы с API конвертации валют требуется ключ доступа.  
Создайте файл `.env` в корне проекта:
API_KEY=your_api_key_here

text

Пример настройки см. в файле `.env.example`.

## Документация:

Подробное описание функций находится в документации проекта

## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE)