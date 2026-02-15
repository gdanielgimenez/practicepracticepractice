# 7.10 dream vacation
dream_vacations = {}
flag = True
while flag:
    name = input("type your name : ")
    place = input("place you would like to go vacation ? ")
    places = []
    dream_vacations[name] = places
    places.append(place)
    more = True
    while more:
        flag_2 = input("would you like to visit more places ? YES-NO ")
        if flag_2 == "yes":
            place = input("place you would like to go vacation ? ")
            places.append(place)
            continue
        else:
            more = False
    contestants = input("would somebody else take the poll ? YES-NO ")
    if contestants == "no":
        flag = False

print(f"-------------------Poll results--------------")
for person, vacation in dream_vacations.items():
    print(f"{person} would love to visit the following places : ")
    for place in vacation:
        print(f"\t{place}")
