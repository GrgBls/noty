def cli():
	import time
	from Tkinter import *

    
	

	print("Welcome to Noty.You can now create sticky notes, easily.")
	time.sleep(2)
	x=raw_input("Type your notes here: ")
	time.sleep(1)
	root = Tk()
	root.title("Noty")
	root.geometry("400x400+50+50")
	Label = Label(root, text=x)
	Label.pack()
	root.mainloop()


