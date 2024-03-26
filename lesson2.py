class Product:

    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price}'


class Cart:

    def __init__(self):
        self.__products = []
        self.__quantity = []

    def add_product(self, product: Product, quantity: int | float = 1):
        self.__products.append(product)
        self.__quantity.append(quantity)

    def remove_product(self, product: Product, quantity: int | float = 1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantity[index] -= quantity
            if self.__quantity[index] <= 0:
                del self.__products[index]
                del self.__quantity[index]

    def total(self):
        total = 0
        for product, quantity in zip(self.__products, self.__quantity):
            total += product.price * quantity
        return total

    def __str__(self):
        if not self.__products:
            return 'Cart is empty'
        return '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                             zip(self.__products, self.__quantity))) +\
               f'\nTotal: {self.total()} UAH'


if __name__ == '__main__':
    product1 = Product('Milk', 25)
    product2 = Product('Bread', 10)
    product3 = Product('Eggs', 20)

    cart = Cart()
    cart.add_product(product1, 2)
    cart.add_product(product2)
    cart.add_product(product3, 3)
    print(cart)

