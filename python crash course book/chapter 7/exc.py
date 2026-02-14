# while loops and user input
# 7.1 Rental car
wanted_car = input("Welcome, what kind of car are you looking for ? " )
print(f"Let me see if i can find you a {wanted_car.title()}")

# 7.2 restaurant 
table_size = input("Goodnight, table for how many ? ")
table_size = int(table_size)
if table_size > 8:
    print(f"We are currently without a table for {table_size} people, youll have to wait ")
else:
    print(f"OK table for {table_size} people, no problem please follow me")

# 7.3 multiples of ten
number = input("Please type a number : ")
if int(number) %10 == 0:
    print(f"your number is a multiple of ten")
else:
    print(f"your number is not a multiple of ten")