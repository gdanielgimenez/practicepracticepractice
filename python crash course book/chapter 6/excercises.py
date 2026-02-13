# 6.1 Person
me = {'first_name': 'Nano', 'lastname': 'gimenez',
      'age': 35, 'location': 'encarnacion'}
for key, item in me.items():
    print(f"{key} : {item}")
print()
# 6.2 favorite numbers
favorite_numbers = {'ana': 5, 'jona': 8, 'gus': 7, 'dani': 99}
for key, item in favorite_numbers.items():
    print(f"{key}'s favorite number is {item}")

# 6.3 Glossary
glossary = {'Boolean': 'a value that can be only True or False',
            'Python': 'a Dynamically typed language',
            'function': 'a block of code that runs when its called',
            }
for key, item in glossary.items():
    print(f"\n{key} : {item}")
