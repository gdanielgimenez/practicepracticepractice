# 5-8 Hello admin
usernames = ["nano", "liam", "admin", "german", "leonard"]
for user in usernames:
    if user == "admin":
        print(f"Welcome back {user}")
    else:
        print(f"you're logged in {user}")

# 5-9 No users
print()
users = ['']
if users:
    print("We need more users")

# 5-10 checking usernames
current_users = ["Nano", "liam", "admin", "german", "leonard"]
new_users = ["batman", "nano", "robin", "eva", "dave"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} username already taken pick another one")
    else:
        print(f"{user} username is available to use.")
# 5-11 ordinal numbers
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
