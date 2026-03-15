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
