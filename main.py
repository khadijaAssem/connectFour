from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox

import numpy as np
import time

class GUI:
    def __init__(self, master):
        # self.v = IntVar()
        self.master = master  # the root object.
        master.title("Connect four")
        master.geometry('570x500')

        # Create button and image
        # btn =  Button(master, text="DFS search", command=lambda: self.solve("dfs", 1))
        # btn.place(x=350, y=300, width=80)  # , height=80)
        # Create button and image
        image = Image.open('bll.jpg')
        image = image.resize((20, 20))
        image = ImageTk.PhotoImage(image)
        login_btn = tk.PhotoImage(file="blackCircle.jpg")
        img = Button(root, image=login_btn, borderwidth=0)

root = Tk()
gui = GUI(root)
root.mainloop()