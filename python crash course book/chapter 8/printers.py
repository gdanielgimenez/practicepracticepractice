def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_desing = unprinted_designs.pop()

        # simulate create a 3d model from the designs
        print(f"printing model {current_desing}")
        completed_designs.append(current_desing)


def show_completed_models(completed_designs):
    print("The following models have been printed.")
    for model in completed_designs:
        print(f"{model}")


def greetings(name):
    print(f"Hello user : {name} you logged in, welcome")
