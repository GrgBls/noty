from tkinter import *

def cli():
	import time
	import datetime
	today = datetime.date.today()
	print("Welcome to Noty.You can now create sticky notes, easily.")
	time.sleep(1.5)
	x=input("Type your notes here: ")
	time.sleep(1)
	#time.sleep prevents GUI from popping up before it receives input.
	root = Tk()
	root.title("Noty")
	root.geometry("300x300")
	#changes the width and height of the GUI.
	Label(root, text=today).pack()
	#prints the input
	Label(root, text=x).pack()
	root.mainloop()
  


