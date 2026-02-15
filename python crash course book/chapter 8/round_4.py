# 8.9 magicians
def show_magicians(magicians):
    for magician in magicians:
        print(f"{magician.title()}")


magicians_names = ['david copperfield', 'harry potter', 'voldemort']
show_magicians(magicians_names)
# 8.10 Great magicians

magicians_names = ['david copperfield', 'harry potter', 'voldemort']


def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("The GREAT "+magician)

    return great_magicians


magicians_names = make_great(magicians_names)
show_magicians(magicians_names)
