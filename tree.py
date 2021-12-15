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
		#app.geometry("2000x1000")
		# set the row height in tkinter treeview
		# s = ttk.Style()
		# s.configure('Treeview', rowheight=(15*self.num_row))
		# Defining title of the app
		s = ttk.Style(app)
		s.configure('Treeview', rowheight=(20 * self.num_row))
		app.title("Minimax Trace")
		# # Defining label of the app and calling a geometry
		# # management method i.e, pack in order to organize
		# # widgets in form of blocks before locating them
		# # in the parent widget
		ttk.Label(app, text="Treeview(hierarchical)").pack()

		# Creating treeview window
		treeview = ttk.Treeview(app)

		# Calling pack method on the treeview
		treeview.pack()

		# Inserting items to the treeview
		# Inserting parent
		keys_list = list(tree)
		total_list = []
		key = keys_list[0]
		# total_list.append(key)
		# z_size = 1
		# w = 0
		# increment_level = 1
		# for i in total_list:
		# 	#display i
		#
		# 	lbl3 = Label(app, text=i)
		# 	lbl3.place(x=(250*(increment_level)/ pow(self.num_col, increment_level-1))* (-z_size)*3, y=150 * increment_level)
		# 	#lbl3.place(x=(1000 / self.num_col) * z_size, y=150 * increment_level)
		# 	z_size -=1
		# 	if i in tree:
		# 		# "Key exists"
		# 		total_list.extend(tree[i])
		# 		w += len(tree[i])
		#
		#
		# 	if (z_size==0):
		# 		increment_level +=1
		# 		z_size = w
		# 		w = 0
		# 	total_list.pop(0)

		treeview.insert('', 0, key, text=key)
		for i in range(len(keys_list)):
			key = keys_list[i]
			for j in range (len(tree[key])):
				if tree[key][j] in tree:
					treeview.insert(str(key), j, tree[key][j], text=tree[key][j])#treeview.insert(str(key), j, tree[key][j], text=tree[key][j])
