def cli():
    import time
    import os
    clear = "\n" * 100
    print("Welcome to noty")
    time.sleep(1)
    print("To create a new note, type N")
    note=raw_input(": ")
    if note=="N" or note=="n":
	    inside=raw_input("Type something on your note!: ")
	    print("Succesfully created a sticke note!")
            time.sleep(1)
	    print clear
	    print (inside)
    else:
	    print("Something went wrong")
	    quit()


