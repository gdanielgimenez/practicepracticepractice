# 3.1 Names
names = ["Gustavo", "German", "Nadia"]
print(names[0])
print(names[1])
print(names[2])

# 3.2 Greetings
print(f"Hello {names[0]} and welcome!")
print(f"Hello {names[1]} and welcome!")
print(f"Hello {names[2]} and welcome!")


# 3.3 own list
fav_transport = ["cars", "bicycle"]
print(f"I like riding {fav_transport[1]}  is good for your health")
print(f"I love {fav_transport[0]} ")

# 3.4 Guest List
dinner_guest = ["Kurt", "Noel", "Paul"]
print(f"{dinner_guest[0]}  you're invited to the dinner.")
print(f"{dinner_guest[1]} you're invited to the dinner.")
print(f"{dinner_guest[2]} you're invited to the dinner.")

# 3.5 changing guest list
print(f"\n{dinner_guest[0]} and {dinner_guest[2]} will not make it to dinner")
dinner_guest[0] = "Liam"
dinner_guest[2] = "Jhon"

print(f"{dinner_guest[0]}  you're invited to the dinner.")
print(f"{dinner_guest[1]} you're invited to the dinner.")
print(f"{dinner_guest[2]} you're invited to the dinner.")

# 3.6
print(f"\nA bigger table was found for the dinner we'll now have 6 guests.")
dinner_guest.insert(0, "Dave")
dinner_guest.insert(2, "Taylor")
dinner_guest.append("Hans")
print(f"{dinner_guest[0]} you're invited to dinner at the new place")
print(f"{dinner_guest[1]} you're invited to dinner at the new place")
print(f"{dinner_guest[2]} you're invited to dinner at the new place")
print(f"{dinner_guest[3]} you're invited to dinner at the new place")
print(f"{dinner_guest[4]} you're invited to dinner at the new place")
print(f"{dinner_guest[5]} you're invited to dinner at the new place")


# 3.7  shriking the guests lists

print("\nUnfortunately we have to reduce the list for only 2 guests.")
uninvited_1 = dinner_guest.pop()
print(
    f"we are sorry for the inconvenient {uninvited_1} your invitation has been cancelled")
uninvited_2 = dinner_guest.pop()
print(
    f"we are sorry for the inconvenient {uninvited_2} your invitation has been cancelled")
uninvited_3 = dinner_guest.pop()
print(
    f"we are sorry for the inconvenient {uninvited_3} your invitation has been cancelled")
uninvited_4 = dinner_guest.pop()
print(
    f"we are sorry for the inconvenient {uninvited_4} your invitation has been cancelled")
print(f"\n{dinner_guest[0]} you're still invited to the dinner")
print(f"\n{dinner_guest[1]} you're still invited to the dinner")
del dinner_guest[0]
del dinner_guest[0]
print(dinner_guest)

# 3.9
dinner_guest = ["liam", "noel", "paul", "jhon", "dave", "ringo"]
print(f"There are {len(dinner_guest)} guests invited to the dinner")

# 3.10 every function
languages = ["english", "spanish", "japanese", "italian", "german"]
print(languages)
lang_one = languages.pop()
print(f"\n{lang_one} was eliminated from the list because i can't speak it")
languages.append("russian")
languages.insert(0, "portuguese")
print(f"\nThe list has been updated : {languages}")
