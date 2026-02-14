# 7.4 pizza toppings
pizza_toppings =[]
flag = True
print("to finish your order please type 'quit' : ")
while flag:
    toppings = input("please select a topping for your pizza? ")
    if toppings == 'quit':
        flag = False
    else:
        pizza_toppings.append(toppings)
print(f"Your requested the following topings for your pizza :")
for topping in pizza_toppings:
    print(f"\t{topping}")

# 7.5 movie tickets
age = int(input("what's your age ? : "))
if age <3:
    print(f"the ticket is free")
elif age <13:
    print(f"the ticket is 10$")
else:
    print(f"the ticket is 15$")

# 7.6 Three exits.

want_more_tickets = True
while want_more_tickets:
    age = int(input("type your age to get a tikcet price : "))
    if age <3:
        print(f"the ticket is free")
    elif age <13:
        print(f"the ticket is 10$")
    else:
        print(f"the ticket is 15$")
    more_tickets = input(f"need more tickets ? yes-no : ")
    if more_tickets == "no":
        want_more_tickets = False

# 7.7 infinity
while True:
 print(f"i've got the infinity stones...")