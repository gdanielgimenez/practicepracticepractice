import json
# simple program to read all files names in a directory and its sub-directories
# ideally stored in a list and create a file
import os
# define the directory path from where we want to create the list.
directory_path = "re-add path for location"
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
# print(book_names)
# print(len(book_names))
# removing duplicates from the list because some are pdfs and epubs
no_duplicates_books = list(set(book_names))
no_duplicates_books = list(no_duplicates_books)
########
# for book in no_duplicates_books:
#    print(book)
# print(len(no_duplicates_books))
#

# update the names of the pdfs.
# next step create a function that compares the .csv file to the list of books on local so we can only leave
# create a list of the missing books on the .csv
current_books = ["buildanapiproduct", "thedesignofwebapis", "designingapiswithswaggerandopenapi", "learncthehardway", "c#andalgorithmicthinkingforthecompletebeginner", "c#interviewguide", "programmingaplswithc#and.net", "c++withoutfear", "learningcoredns", "cloudpenetrationtesting", "pentestingapis", "cybersecurityblueteamstrategies", "grokkingwebapplicationsecurity", "dockerup&running", "graphqlbestpractices", "fullstackgraphqlapplications", "greppocketreference", "webdesignplayground", "97thingseveryjavaprogrammershouldknow", "javacookbook", "learningjava", "thinkjava", "reactivesystemsinjava", "springboot3.0cookbook", "begintocodewithjavascript", "d3.jsinaction", "functionalprogramminginjavascript", "getprogrammingwithjavascript",
                 "thejamstackbook", "javascriptonthings", "secretsofthejavascriptninjas", "singlepagewebapplications", "classicshellscripting", "learningthebashshell", "linuxdevicedrivers", "linuxinanutshell", "linuxsystemprogramming", "unixpowertools", "networkprogrammabilityandautomation", "postgresql:upandrunning", "learnpythonthehardway", "thinkpython", "pythoncrashcourse", "reacthooksinaction", "reactindepth", "reactquickly", "railscrashcourse", "rubybyexample", "rubyonrailstutorial7e", "rustwebdevelopment", "theartofunittestingwithexamplesinjs", "essentialtypescript5", "buildafrontendframework", "buildinguserfriendlydsls", "c++highperformance", "thec++workshop", "begginingc++gameprogramming", "shellprogramminginlinuxunixandosx", "tcp/ipillustratedvolume1"]
books_json = []
with open("books.json") as f_obj:
    books_json = json.load(f_obj)
print(f"fom json file")
print(books_json)


def missing_books(list1, list2):
    not_listed = []
    for book in list1:
        if book not in list2:
            not_listed.append(book)
    print("the following items are missing from the list.")
    print(f"there's a total of {len(not_listed)} items")
    for item in not_listed:
        print(item)


# test.
# list1 = ['eggs', 'milk', 'honey']
# list2 = ['eggs', 'milk', 'honey', 'sugar', "flour"]
# missing_books(list2, list1)
# function call to check both lists.
# missing_books(no_duplicates_books, current_books)
#
