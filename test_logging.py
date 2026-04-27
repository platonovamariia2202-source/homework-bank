from src import masks, utils

# Тестируем masks
masks.get_mask_card_number("1234567890123456")
masks.get_mask_card_number("")
masks.get_mask_account("9876543210")
masks.get_mask_account("")

# Тестируем utils
utils.get_transactions_from_json("data/operations.json")
utils.get_transactions_from_json("nonexistent.json")
