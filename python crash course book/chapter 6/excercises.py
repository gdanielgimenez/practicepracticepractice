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


# 6.4 Glossary 2 adding new values to 6.3
glossary['int'] = "integer number values"
glossary['float'] = "float number values"
glossary['import'] = "Keyword used to import modules"

for key, item in glossary.items():
    print(f"\n{key} : {item}")

# 6.5 Rivers
print()
rivers = {'nile': 'egypt', 'missisipi': 'usa', 'amazon': 'brazil'}
# 6.5.1 sentences
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}")

print()
# only keys default behavtior when priting dictionaries
for river in rivers:
    print(river)

print()
# only items
for country in rivers.values():
    print(country)


# 6.6 Polling
favorite_languages = {'jona': 'C', 'michael': 'C++', 'jhonny': 'JAVA'}
students = ['jona', 'steven', 'Madds', 'Sven']

for student in students:
    if student in favorite_languages:
        print(f"Thanks for taking the poll {student}")
    else:
        print(f"you should consider take the poll {student}")
