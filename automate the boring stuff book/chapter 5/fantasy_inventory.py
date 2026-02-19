# chapter 5 practice projects assigments page 120
# write a function that displays all items in inventory +  total number of items
def display_inventory(inventory):
    items_total = 0
    print("inventory :")
    for key, value in inventory.items():
        print(f"{value} {key}")
        items_total += int(value)
    print(f"Total number of items : {items_total}")


# inventory
player_inventory = {'rope': 1, 'torch': 6,
                    'gold coins': 42, 'dagger': 1, 'arrow': 12}
# function call
display_inventory(player_inventory)
# part 2 of the assigment
# write a function named addToInventory(inventory, addedItems)
dragon_loot = ['gold coins', 'dagger', 'gold coins', 'gold coins', 'ruby']


def add_to_inventory(inventory, loots):
    for loot in loots:
        if loot in inventory.keys():
            inventory[loot] += 1
        else:
            inventory[loot] = 1

    print(f"loot added to inventory")


add_to_inventory(player_inventory, dragon_loot)
display_inventory(player_inventory)
