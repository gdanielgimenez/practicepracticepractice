# 8.1 Message
def display_message():
    print(f"This chapter is all about functions.")


display_message()

# 8.2 favorite books.


def favorite_book(book):
    print(f"One of my favorrite books is {book}")


favorite_book("Alice in Wonderland")
favorite_book("1984")

# 8.3 T-shirt


def make_shirt(size, message):
    print(f"T-shirt size : {size} with the message {message}")


make_shirt("m", "Live forever")
make_shirt(message="Live forever", size="XL")

# 8.4 Large shirts


def make_shirt_2(size="large", message="i love python"):
    print(f"T-shirt size : {size} with the message {message}")


# three different calls
make_shirt_2()
make_shirt_2(size="medium")
make_shirt_2("small", "time to learn JAVA")

# 8.5 cities


def describe_city(city, country="USA"):
    message = f"{city} is located in the country of {country}"
    print(message)


describe_city("New York")
describe_city("Alaska")
describe_city("Manchester", "UK")
