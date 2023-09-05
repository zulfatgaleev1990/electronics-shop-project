"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


Item.pay_rate = 0.75
@pytest.fixture
def smartphone_info():
    return Item("smartphone", 25000, 8)


def test_calculate_total_price(smartphone_info):
    assert smartphone_info.calculate_total_price() == 200000.0


def test_apply_discount(smartphone_info):
    assert smartphone_info.apply_discount() == None
