from menu_item import MenuItem

menu_item1 = MenuItem('Burger Sushi', 100)
menu_item2 = MenuItem('Narutoki', 500)
menu_items = [menu_item1, menu_item2]

for menu in menu_items:
    print(menu.info())