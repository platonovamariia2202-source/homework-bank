from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """масирует информацию о картах и о счетах."""

    full_card = account_card.rsplit(" ", 1)
    name = full_card[0]
    number = full_card[1]
    if "Счет" in name:
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_line: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    date_part = date_line[:10]
    parts = date_part.split("-")

    return f"{parts[2]}.{parts[1]}.{parts[0]}"
