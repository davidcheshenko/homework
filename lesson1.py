import dataclasses


@dataclasses.dataclass
class Dish:
    name: str
    price: float | int


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))


class Menu:
    def __init__(self, name: str):
        self.name = name
        self.__categories = []

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__categories))


dish_1 = Dish(name="Pizza", price=12.5)
dish_2 = Dish(name="Pasta", price=8)
dish_3 = Dish(name="Salad", price=5.5)
dish_4 = Dish(name="Soup", price=4.5)
dish_5 = Dish(name="Steak", price=15)
dish_6 = Dish(name="Fish", price=10)
dish_7 = Dish(name="Sushi", price=20)


category_1 = Category(name="Main Course")
category_2 = Category(name="Appetizer")

category_1.add_dish(dish_1)
category_1.add_dish(dish_2)
category_1.add_dish(dish_3)
category_2.add_dish(dish_4)
category_2.add_dish(dish_5)
category_2.add_dish(dish_6)
category_2.add_dish(dish_7)

menu = Menu(name="Restaurant Menu")
menu.add_category(category_1)
menu.add_category(category_2)

print(menu)


