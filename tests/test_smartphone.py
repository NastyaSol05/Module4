from typing import Any

import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture
def smartphone() -> Any:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return smartphone1 + smartphone2


def test_add_smartphone(smartphone: Any) -> None:
    assert smartphone == 2580000.0


def test_add_grass_smartphone() -> None:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    try:
        smartphone1 + grass1
    except TypeError:
        assert True
