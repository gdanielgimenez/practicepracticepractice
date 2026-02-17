# imported Restaurant
from privileges import Administrator as adm
from modules import Administrator
from modules import Restaurant

mcdonadls = Restaurant("mcdonald's", "fast food", 100)
mcdonadls.describe_restaurant()

# imported admin

batman = Administrator("bruce", "wayne", "bman@gmail.com", 45, "gotham city",
                       ["ban users", "create users", "create posts", "delete posts"])
batman.privileges.show_privileges()

# 9-12 multiple modules import
# create an admin importing from privileges which imports its parent class from user.py
robin = adm("bruce", "wayne", "bman@gmail.com", 45, "gotham city",
            ["ban users", "create users", "create posts", "delete posts"])
robin.privileges.show_privileges()

# all working as expected
