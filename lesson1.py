class Product:

    def__init__(self,name:str,price: int|float) 
       self.name = name
       self.price = price  



    def__str__(self)
        return f'{self.name}: {self.price}'



pr_1 = Product(phone,500)        


class Cart:
    def__init__(self):
        self.__products = []
        self.__quantity = []


    def add_product(self, product:Product, quantity = int|float = 1)
        self.__products.append(product)
        self.__quantity.append(quantity)
    
     
     def remuve_product(self,product: Product, quantity = int| float = 1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantity[index] += quantity
            if self.__quantity[index] <= 0
               del self.products[index]
               del self.quantity[index]




    def total(self):
        total = 0
        for product,quantity in zip(self.__products,self__quantity):
            total += product.price * quantity 
        return total 


    def__str__(self):
        if not self.__products
           return 'Cart is ampty'
           



