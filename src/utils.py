import json
import logging
from typing import Any, Dict, List

# 1. Настройка логера для модуля utils
logger_utils = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)  # Уровень DEBUG и выше

# 2. Настройка file_handler (куда и как пишем)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# 3. Настройка formatter (что именно пишем)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# 4. Связываем handler и логер
logger_utils.addHandler(file_handler)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций."""
    logger_utils.info(f"Попытка открыть файл: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger_utils.debug(f"JSON успешно загружен из {file_path}")
    except FileNotFoundError:
        logger_utils.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger_utils.error(f"Ошибка декодирования JSON: {e}. Файл: {file_path}")
        return []

    if isinstance(data, list):
        logger_utils.info(f"Данные из {file_path} являются списком. Количество транзакций: {len(data)}")
        return data
    else:
        logger_utils.warning(f"Данные в файле {file_path} не являются списком. Возвращаем пустой список.")
        return []
