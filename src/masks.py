import logging

# Настройка логера для masks
logger_masks = logging.getLogger("masks")
logger_masks.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_masks.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    logger_masks.info(f"Попытка маскировки карты: {card_number}")

    if not card_number:
        logger_masks.error("Передан пустой номер карты")
        return ""

    try:
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger_masks.debug(f"Успешная маскировка: {masked}")
        return masked
    except Exception as e:
        logger_masks.error(f"Ошибка маскировки карты {card_number}: {e}", exc_info=True)
        return ""


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта."""
    logger_masks.info(f"Попытка маскировки счета: {account_number}")

    if not account_number:
        logger_masks.error("Передан пустой номер счета")
        return ""

    try:
        masked = f"**{account_number[-4:]}"
        logger_masks.debug(f"Успешная маскировка счета: {masked}")
        return masked
    except Exception as e:
        logger_masks.error(f"Ошибка маскировки счета {account_number}: {e}", exc_info=True)
        return ""
