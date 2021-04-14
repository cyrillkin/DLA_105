# Предметная область – магазин.
# Разработать класс Shop, описывающий работу магазина продуктов.
# Разработать класс Products, продукт описывается следующими параметрами:
# уникальный идентификатор, название продукта, стоимость, количество.
# Разработать класс FruitProduct на базе класс Product, фрукт характеризуется параметрами:
# страна изготовителя, срок годности.

class Shop:
    pass

class Products:
    def __init__(self, id_product, name_product, price, count):
        self.id_product = id_product
        self.name_product = name_product
        self.price = price
        self.count = count

        pass

class FruitProduct(Products):
    def __init__(self, made_country, expiration):
        self.made_country = made_country
        self.expiration = expiration

    pass