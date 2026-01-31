def calc_discount(price, percent):
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    if percent < 0 or percent > 100:
        raise ValueError("Процент должен быть от 0 до 100")

    return price - price * percent / 100


def calc_total(price, quantity):
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")

    return price * quantity
