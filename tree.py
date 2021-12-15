# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import *
import tkinter.font as tkFont
# Importing ttk from tkinter
from tkinter import ttk
class plot:
	my_tree = {}

	def __init__(self, num_row, num_col):
		# assume index from 0 to < n.
		self.num_row = num_row
		self.num_col = num_col
		return
	def set_tree(self, tree):
		# Creating app window
		app = Tk()
		s = ttk.Style(app)
		s.configure('Treeview', rowheight=(19 * self.num_row))
		app.title("Minimax Trace")
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
				if tree[key][j] in tree:
					treeview.insert(str(key), j, tree[key][j], text=tree[key][j])#treeview.insert(str(key), j, tree[key][j], text=tree[key][j])
