# 6.7 People
person_1 = {'name': 'gustavo',
            'lastname': 'gimenez', 'age': 35, 'location': 'Py'}
person_2 = {'name': 'dani',
            'lastname': 'benitez', 'age': 23, 'location': 'USA'}
person_3 = {'name': 'jon',
            'lastname': 'smith', 'age': 45, 'location': 'USA'}

# list of dictionaries
people = [person_1, person_2, person_3]

for person in people:
    print(f"Name : {person['name']}")
    print(f"Last Name : {person['lastname']}")
    print(f"Age : {person['age']}")
    print(f"Location : {person['location']}")
    print()

# 6.8 Pets
puckens = {'name': 'puckito', 'animal': 'dog', 'owner': 'An'}
tito = {'name': 'tito', 'animal': 'cat', 'owner': 'Unknown'}
tina = {'name': 'tina', 'animal': 'dog', 'owner': 'Tia'}

pets = [puckens, tito, tina]

# looping the list

for pet in pets:
    print(f"pet : {pet['name']}")
    print(f"type : {pet['animal']}")
    print(f"owner : {pet['owner']}\n")


# 6.9 favorite places
favorite_places = {"nano": ['Bs As', 'Asc', 'enc'],
                   "jhonny": ['arizona', 'paris'], "lily": ['italy']}

# looping
for person, city in favorite_places.items():
    print(f"{person}'s favorite places are : ")
    for item in city:
        print(f"\t{item}")

# 6.10 favorite numbers
favorite_numbers = {'jona': [1, 2, 3],
                    'james': [7, 14, 21], 'jonathan': [5, 99], }

# loop through
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are : ")
    for number in numbers:
        print(f"\t{number}")


# 6.11 Cities
cities = {'Buenos Aires': {'country': 'Argentina', 'population': '12.000.000', 'fact': 'greatest place on earth to go to a concert'},
          'Asuncion': {'country': 'Paraguay', 'population': '350.000', 'fact': 'very dangerous when it rains'},
          'Manchester': {'country': 'United Kingdom', 'population': '7.000.000', 'fact': 'birth place of Oasis'}}

# loop to show information
for city, info in cities.items():
    print(f"{city} general information.")
    for key, item in info.items():
        print(f"{key} : {item}")
    print()


# 6.12 Extensions see for later
