import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    """Тест на корректную работу маскировки карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

def test_get_mask_card_number_short():
    """Тест на короткий номер карты"""
    assert get_mask_card_number("12345678") == "1234 56** **** 5678"

def test_get_mask_card_number_empty():
    """Тест на пустую строку"""
    assert get_mask_card_number("") == ""

def test_get_mask_account():
    """Тест на корректную работу маскировки счета"""
    assert get_mask_account("73654108430135874305") == "**4305"

def test_get_mask_account_short():
    """Тест на короткий номер счёта"""
    assert get_mask_account("123") == "**123"

def test_get_mask_account_empty():
    """Тест на пустую строку"""
    assert get_mask_account("") == "**"