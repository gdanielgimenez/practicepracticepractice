# 8.12 sandwiches
def sandwiches_ingredients(*ingredients):
    print(f"\norder finalized. your sandwich will have the following ingredients :")
    for ingredient in ingredients:
        print(f"\t{ingredient}")


# function calls with different amount of parameters
sandwiches_ingredients("ham", "cheese", "tomatoes")
sandwiches_ingredients("sausage", "meat", "chips", "ham", "cheese", "tomatoes")
sandwiches_ingredients("cheese", "lettuce")

# 8.13 user profile


def build_profile(first, last, **user_info):
    """builds a dictionary with all known info about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# function call with at least 5 arguments
user_nano = build_profile('nano', 'gimenez',
                          age=35,
                          location='py',
                          field='programming',
                          languages=['python', 'JAVA'])
print(user_nano)


# 8.14 Cars

def build_car(maker, model, **car_info):
    car = {}
    car['maker'] = maker
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


# function call to build cars with diff number of arguments
my_toyota = build_car('toyota', 'supra', year='1998',
                      transmision='manual', color='white')
print(my_toyota)
my_ferrari = build_car('Ferrari', 'F-50', color='red')
print(my_ferrari)
porsche = build_car("Porsche", '911 GT-3')
print(porsche)
