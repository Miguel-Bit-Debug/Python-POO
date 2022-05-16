class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)

    #Getter
    @property
    def price(self):
        return self._price

    #Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value



p1 = Product('Camiseta', 50)

p1.discount(10)

print(p1.price)

p2 = Product('Caneta', 'R$15')

p2.discount(10)

print(p2.price)