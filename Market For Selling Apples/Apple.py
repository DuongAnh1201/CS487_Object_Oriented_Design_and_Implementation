class Apple:
    def __init__(self, type, weight, price):
        self.__type = type
        self.__weight = weight
        self.__price = price
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Price must be > 0')
        else:
            self.__price = price
    
    @property
    def weight(self): return self.__weight
    @property
    def type(self): return self.__type
    def __str__(self):
        return self.__type + ', ' + '{:.2f}'.format(self.__weight) + ', '+'{:.2f}'.format(self.__price)

    