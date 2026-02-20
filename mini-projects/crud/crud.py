# user can create save delete or update to do list.
# v1 start with only one list.
to_do_list = []
to_do_dict = {}
# we transform out list into a dict where task are keys and values are completed or not
active = True
while active:
    choice = input(
        "\nTo add items to the list type 'a' \nTo edit items type 'e' \nTo delete items type 'd' \nTo quit the program type 'q' \n: ")
    if choice.lower() == 'q':
        print("Goodbye!")
        active = False
    elif choice == 'a':
        print("type down and then press enter to ad items to the list")
        item = input(" item : ")
        to_do_list.append(item)
        # add to dict turn later into a funct
        to_do_dict[item] = "Not completed"
        print("------------------item added to the list-------------------- ")
        # print the current list
        print("Here's the current list : ")
        i = 0
        for key, value in to_do_dict.items():
            i += 1
            print(f"\t {i}. {key} : {value}")
        print("------------------------------------------------------------ ")
    elif choice == 'e':
        edit_mode = input("type 'e' to edit mode or 's' for change status : ")
        # print the current list
        print("Here's the current list : ")
        print("-------------------------------------- ")
        i = 0
        for key, value in to_do_dict.items():
            i += 1
            print(f"\t {i}. {key} : {value}")
        print("------------------------------------------------------------ ")
        if edit_mode == 'e':
            print("edit mode : type item number to edit ")
            task_number = int(input(" : "))
            new_value = input("type in the corrected task : ")
            key_finder = to_do_list[task_number-1]
            del to_do_dict[key_finder]
            to_do_dict[new_value] = "Not completed"
            to_do_list[task_number-1] = new_value
            # add logic to edit entry use index to realte to dict from list
        elif edit_mode == 's':
            print("status mode : type item number ")
            task_number = int(input(" : "))
            key_finder = to_do_list[task_number-1]
            to_do_dict[key_finder] = "Completed"
    elif choice == 'd':
        # print the current list
        print("Here's the current list : ")
        print("---------------------delete mode---------------------------- ")
        i = 0
        for key, value in to_do_dict.items():
            i += 1
            print(f"\t {i}. {key} : {value}")
        print("------------------------------------------------------------ ")
        print("delete mode : type item number to edit ")
        item_number = int(input(" : "))
        del to_do_dict[to_do_list[item_number-1]]
        del to_do_list[item_number-1]
