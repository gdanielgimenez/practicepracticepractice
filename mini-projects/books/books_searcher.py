# list of books or dictionary
books_info = []  # start with titles only
book_titles = []
# step one  given a list, a dictionary or any other kind of document we should be able to input
# a book name and get a response if the book is already there.

# step 2 give the option to add new books
filename = "e-books list.csv"

with open(filename) as file_object:
    for line in file_object:
        # print(line)
        book = ([line.lower().split(",")])
        if '"' not in book[0][0]:
            books_info.append(book[0][0])
    # print(books_info)
# books_info has 66 lists items
# print(books_info[2][0][0])
# title = books_info[2][0].split(",")
# print(title)
# print(books_info)
book_titles = books_info[2:61]
print(book_titles)
# for title in book_titles:
#    print(title)
print(len(book_titles))

active_search = True
while active_search:
    book_name = input(
        "Type the book title to check if it is already in the list : ")
    if book_name in book_titles:
        print(f"{book_name} already in the list")
    else:
        print(
            f"The book {book_name} is not currenlty on the list, please add it to it")
    search = input(f"\ntype YES to search another book, NO to quit program :")
    if search == "no":
        active_search = False
