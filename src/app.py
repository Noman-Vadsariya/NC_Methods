from tkinter import *
from tkinter import ttk

class App:
	def __init__(self):
		self.root = Tk()

	def setTitle(self, title = ""):
		self.root.title(title)



root = Tk()
root.title("Hello World")

mainframe = ttk.Notebook(root)
f1 = ttk.Frame(mainframe)
f2 = ttk.Frame(mainframe)
mainframe.add(f1, text = "Menu")
mainframe.add(f2, text = "Menu2")

def run(app):
	app.mainloop()
