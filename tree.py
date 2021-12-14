# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import *

# Importing ttk from tkinter
from tkinter import ttk
class plot:
	my_tree = {}
	def set_tree( tree):
		# Creating app window
		app = Tk()

		# Defining title of the app
		app.title("GUI Application of Python")

		# Defining label of the app and calling a geometry
		# management method i.e, pack in order to organize
		# widgets in form of blocks before locating them
		# in the parent widget
		ttk.Label(app, text="Treeview(hierarchical)").pack()

		# Creating treeview window
		treeview = ttk.Treeview(app)

		# Calling pack method on the treeview
		treeview.pack()

		# Inserting items to the treeview
		# Inserting parent
		keys_list = list(tree)
		key = keys_list[0]
		treeview.insert('', 0, key, text=key)
		for i in range(len(keys_list)):
			key = keys_list[i]
			for j in range (len(tree[key])):
				treeview.insert(str(key), j, tree[key][j], text=tree[key][j])

		# Calling main()
		app.mainloop()
