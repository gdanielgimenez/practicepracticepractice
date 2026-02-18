# simple program to read all files names in a directory and its sub-directories
# ideally stored in a list and create a file
import os
# define the directory path from where we want to create the list.
directory_path = "re-add path to files"
book_names = []


folder_names = os.listdir(directory_path)
for name in folder_names:
    # print(f"{name}")
    sub_folder = directory_path+f"/{name}"
    books_to_add = os.listdir(sub_folder)
    for book in books_to_add:
        # print(f"{book.replace(".pdf", "")}")
        book_names.append(book.replace(".pdf", "").replace(".epub", ""))
# full list of books in directory's sub-directories without extensions
# for book in book_names:
#    print(f"{book}")
print(book_names)
print(len(book_names))
# removing duplicates from the list because some are pdfs and epubs
no_duplicates_books = list(set(book_names))
for book in no_duplicates_books:
    print(book)
print(len(no_duplicates_books))

# update the names of the pdfs.
# next step create a function that compares the .csv file to the list of books on local so we can only leave
# or create a list of the missing books on the .csv
