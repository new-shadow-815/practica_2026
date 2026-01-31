"""
Модуль marketplace

Содержит базовые классы для работы с товарами и корзиной:
- Product — товар
- Cart — корзина покупателя
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Product:
    """
Товар.

:param name: Название товара.
:param price: Цена за единицу.
:param quantity: Количество.

    """

    name: str
    price: float
    quantity: int = 1

    def increase(self) -> None:
        """
        Увеличить количество товара.

        """
        self.quantity += 1

    def decrease(self) -> None:
        """
        Уменьшить количество товара.

        """

        self.quantity -= 1

        if self.quantity < 0:
            self.quantity = 0

    @property
    def total_price(self) -> float:
        """
        Стоимость позиции.
        """
        return self.price * self.quantity


class Cart:
    """
    Корзина покупателя.
    """

    def __init__(self) -> None:
        self.items: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """
        Добавить товар в корзину.

        Если товар уже есть — увеличивает количество.

        :param product: Товар.
        """

        if product.name in self.items:
            self.items[product.name].increase()
        else:
            self.items[product.name] = product

    def remove_product(self, product_name: str) -> None:
        """
        Удалить товар из корзины полностью.

        :param product_name: Название товара.
        """
        self.items.pop(product_name, None)

    def increase_quantity(self, product_name: str) -> None:
        """
        Увеличить количество товара.

        :param product_name: Название товара.
        """
        if product_name not in self.items:
            raise KeyError("Товар не найден в корзине")

        self.items[product_name].increase()

    def decrease_quantity(self, product_name: str) -> None:
        """
        Уменьшить количество товара.

        Если количество станет 0 — товар удаляется.

        :param product_name: Название товара.
        """
        if product_name not in self.items:
            raise KeyError("Товар не найден в корзине")

        item = self.items[product_name]
        item.decrease()

        if item.quantity < 0:
            item.quantity = 0

        if item.quantity == 0:
            self.remove_product(product_name)

    def total_sum(self) -> float:
        """
        Общая сумма корзины.
        """
        return sum(item.total_price for item in self.items.values())
