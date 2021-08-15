def searcher():
    import time
    letter1 = "This is the letter for the Abhinav Namdeo"
    letter2 = "This is the letter for the Ashutosh Namdeo"
    letter3 = "This is the letter for the Abhishek Namdeo"
    letter4 = "This is the letter for the Manju Namdeo"
    time.sleep(3)

    while True:
        # text = input("Search here\n")
        text = (yield )
        if text in letter1:
            print("Your letter is letter1")
        elif text in letter2:
            print("Your letter is letter2")
        elif text in letter3:
            print("Your letter is letter3")
        elif text in letter4:
            print("Your letter is letter4")
        else:
            print("There is no letter for you")

search = searcher()
next(search)
search.send("Abhinav Namdeo")
input("Press any key")
search.send("Abhishek Namdeo")


