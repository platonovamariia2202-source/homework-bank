import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card_card():
    """Тест на маскировку карты"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account():
    """Тест на маскировка счёта"""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_get_date_normal():
    """Тест на корректную дату"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty():
    """Тест на пустую строку"""
    assert get_date("") == ""
