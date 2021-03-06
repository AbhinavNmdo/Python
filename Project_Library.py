import time


def logcat(msg):
    with open("LibraryLog.txt", "a") as f:
        f.write(f"{msg} at {time.asctime()}\n")


class AbhayLibrary:

    def library(self):
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the Abhay's Library")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nWhats Your Name Sir/Madam")
        name = input()
        print("\n\t\t\tNotes")
        print("____________________________")
        print("| Type 'books' to know     |")
        print("| Type 'issue' to Issue    |")
        print("| Type 'add' to Add        |")
        print("| Type 'return' to Return  |")
        print("| Type 'donate' to Donate  |")
        print("| Type 'exit' to Donate    |")
        print("----------------------------")

        availableBooks = {"Java", "Python"}

        while True:
            print("\nEnter value as Notes")
            user = input()

            if user == "books":
                print("Available Books are Mentioned below")
                print(availableBooks)

            elif user == "add":
                print("Type 'exit' to exit in main menu")
                print("Enter book name to Add in the library")
                bookname = input()
                if bookname == "exit":
                    continue
                else:
                    if bookname in availableBooks:
                        print("Sorry, this book is already available")
                        print("------------------------------------------------")
                    else:
                        availableBooks.add(bookname)
                        logcat(f"{name} Add {bookname} book")
                        print("Your Book is Added Successfully")
                        print("------------------------------------------------")

            elif user == "return":
                print("Enter the book name to return")
                bookname = input()
                availableBooks.add(bookname)
                logcat(f"{name} Return {bookname} book")
                print("Your Book is Returned Successfully")
                print("------------------------------------------------")

            elif user == "donate":
                print("Type 'exit' to exit in main menu")
                print("Enter the book name to Donate")
                bookname = input()
                if bookname == "exit":
                    continue
                else:
                    if bookname in availableBooks:
                        print("Sorry, this book is already in the library")
                        print("------------------------------------------------")
                    else:
                        availableBooks.add(bookname)
                        logcat(f"{name} Return {bookname} book")
                        print("Your Book is Donated Successfully")
                        print("------------------------------------------------")


            elif user == "issue":
                print("Type 'exit' to exit in main menu")
                print("Enter the book name to Issue")
                bookname = input()
                if bookname == "exit":
                    continue
                else:
                    if bookname in availableBooks:
                        availableBooks.remove(bookname)
                        logcat(f"{name} Issue {bookname} book")
                        print("Your Book is Issued Successfully")
                        print("------------------------------------------------")
                    else:
                        print("Sorry, this Book is not available in the Library")
                        print("------------------------------------------------")


            elif user == "notes":
                print("\n\t\t\tNotes")
                print("----------------------------")
                print("| Type 'books' to know     |")
                print("| Type 'issue' to Issue    |")
                print("| Type 'add' to Add        |")
                print("| Type 'return' to Return  |")
                print("| Type 'donate' to Donate  |")
                print("----------------------------")

            elif user == "exit":
                print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThanks {name} to Visiting Abhay's Library")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                break

            else:
                print("Enter valid value as Notes")



abhay = AbhayLibrary()
abhay.library()
