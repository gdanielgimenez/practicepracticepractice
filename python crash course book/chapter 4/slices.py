# 4.10 pizzas =['pepperoni','muzzarella',"extra cheese", "margarita"]
pizzas =['pepperoni','muzzarella',"extra cheese", "margarita", "chicken pizza"]
print(f"\nThe first 3 pizzas are : ")
print(pizzas[0:3])
print(f"\nThe middle 3 pizzas are : ")
print(pizzas[1:4])
print(f"\nThe last  3 pizzas are : ")
print(pizzas[2:5])


# 4.11 my pizza your pizzas

pizzas =['pepperoni','muzzarella',"extra cheese", "margarita", "chicken pizza"]
friends_pizzas = pizzas[:]
pizzas.append("pineapple")
friends_pizzas.append("Double Cheese")

print("my favorite pizzas are : ")
for pizza in pizzas:
    print(pizza)
print()
print("MY fiend's favorite pizzas are : ")
for pizza in friends_pizzas:
    print(pizza)

# 4.12 
favorite_foods =["pizza" ,"cake and coffee","sandwiches","milanesa", "hamburguers"]
print()
for food in favorite_foods:
    print(food)