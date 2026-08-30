import Apple
class Barrel:
    def __init__(self, capacity):
        self.__list = []
        self.__capacity = capacity
    
    @property
    def list(self): return self.__list
    @list.setter
    def list(self, l): 
        self.__list = l
    @property
    def capacity(self): return self.__capacity
    def get_total_weight(self):
        total = 0.0
        for apple in self.list:
            total += apple.weight
        return total
    
    def add_apple(self, apple):
        if self.get_total_weight() + apple.weight > self.capacity:
            print("Error! Exceeds capacity.")
            return False
        self.list.append(apple)
        return True

    def get_barrel_price(self):
        '''
        TODO: Accumulate and return total price
        '''
        total_price = 0
        for apple in self.list:
            total_price += apple.price()
        return total_price

    def remove_small_apples(self):
        '''
        TODO: Remove all apples under 0.5 lb
        '''
        remaining_apple = [
            apple for apple in self.list if apple.weight >= 0.5
        ]
        self.list = remaining_apple

    def __str__(self):
        output = 'capacity: ' + '{:2f}'.format(self.capacity) + '\n'
        for apple in self.list:
            output += str(apple) + '\n'
        return output

    