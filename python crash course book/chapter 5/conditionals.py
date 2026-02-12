# 5.1  conditional tests
car = "subaru"
print(f"is car ==  subaru? i predict true")
print(car == "subaru")

print(f"is car ==  audi? i predict False.")
print(car == "audi")

# create ten tests at least five  of each one
snoopy = "dog"
garfield = "cat"
scooby = "dog"
lassie = "dog"
taz ="tasmanian devil"
print(f"is snoopy a dog ?", snoopy =="dog")
print(f"is snoopy a cat ?", snoopy =="cat")
print(f"is gardfield a dog ?", garfield =="dog")
print(f"is gardfield a cat ?", garfield =="cat")
print(f"is scooby a dog ?", scooby =="dog")
print(f"is scooby a cat ?", scooby =="cat")
print(f"is taz a dog ?", taz =="dog")
print(f"is taz a cat ?", taz =="cat")

# 5.2 more conditional tests
singer = "Liam"
writer = "Noel"
print(singer == writer)
print(writer == "Noel")
print(singer.lower() == "liam")
# numerical
print(10>5)
print(10< 5)
print(5 == 5)
print(6<= 5)
print(3>=2)
oasis = ["Liam", "Noel","bonehead","andy", "gem"]
if "guigsy" in oasis:
    print("Welcome back to Oasis Guigs")

if "guigsy" not in oasis:
    print("Guigs have not come back for the reunion tour")
# and  or
if (5>6) and 5>4:
    print("five rocks")

if 5>3 or 5>4:
    print("max number is five")