class MenuItem:
    def __init__ (self,name):
        self.name = name
    def hello(self):
        print('Hello '+self.name)

menu_item1 = MenuItem('Stanley')
menu_item1.hello()