foods = ['pasta', 'burger', 'sushi']
print(foods[2])

foods.append('noruki')
print(foods)

for food in foods :
    print('I like '+food)

fruits = {'apple':'red', 'banana':'yellow','grape':'purple'}
for fruit in fruits :
    print(fruit+ ' is '+fruits[fruit])

x = 1
while x < 10:
    print(x)
    if x == 3:
        print('This is 3')
    elif x == 8:
        break
    x+=1