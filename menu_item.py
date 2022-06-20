class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print('I eat '+self.name)
        print('food price is '+str(self.price))