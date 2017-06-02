def cli():
	import time 
	from Tkinter import * #imports time library and Tkinter library.

    


	print("Welcome to Noty.You can now create sticky notes, easily.") #Prints the text.
	time.sleep(2)
	x=raw_input("Type your notes here: ") #Asks for user input.
	time.sleep(1)
	root = Tk()
	root.title("Noty") #Changes the GUI title to Noty.
	root.geometry("400x400+50+50") #Changes the width and the height of the GUI.
	Label = Label(root, text=x) #Prints the previous input(x)
	Label.pack() #Packs the label
	root.mainloop()


