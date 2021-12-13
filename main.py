from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox
import gameAlgorithm

import numpy as np
import time

  # self.gameboard_pl(master)

# self.img = ImageTk.PhotoImage(Image.open("blackCircle.jpg"))  # PIL solution
# canvas.create_image(20,20, anchor=NW, image=self.img)  
# img.place(x=350, y=300, width=80)  # , height=80)

# Create button and image
# btn =  Button(master, text="DFS search", command=lambda: self.solve("dfs", 1))
# btn.place(x=350, y=300, width=80)  # , height=80)
# Create button and image
# image = Image.open("blackCircle.jpg")
# image = image.resize((20, 20))
# image = ImageTk.PhotoImage(image)
# image.place(x=350, y=300, width=80)  # , height=80)
# login_btn = tk.PhotoImage(file="blackCircle.jpg")
# img = Button(root, image=self.img, borderwidth=0)
# img.place(x=350, y=300, width=80)

class GUI:

    backgroundColor = "#051094"
    whiteColor = "#FFFFFF"
    blackColor = "#000000"
    redColor = "Red"
    greenColor = "Green"
    numOfRows = 6
    numOfCols = 7
    humanColor = greenColor
    colors = [greenColor, redColor]
    canvasWidth = 570
    canvasHeight = 500
    wScale = 1
    hScale = 1
    lastRow = [0]*numOfCols
    # 0 for human(red) 1 for computer(green)
    turn = False

    def __init__(self, master):
        self.board = '2'*(self.numOfRows * self.numOfCols) #[[-1]*self.numOfCols for i in range(self.numOfRows)]
        
        self.master = master  # the root object.
        master.title("Connect four")
        self.canvas = Canvas(master, width=self.canvasWidth, height=self.canvasHeight, background=self.backgroundColor, highlightthickness=0)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.create_grid)
    
    def allBlack(self, event=None):
        if (len(self.canvas.find_withtag("circles")) != 0):
            self.canvas.scale("circles",0,0,self.wScale,self.hScale)
            return

        for i in range (0, self.numOfRows):
            for j in range (0, self.numOfCols):
                self.putCircle(i, j, self.blackColor)

    def putCircle(self, row, col, color):
        marginH = self.canvasHeight/100
        marginW = self.canvasWidth/150

        x0 = col * (self.canvasWidth // self.numOfCols)+marginW
        y0 = row * (self.canvasHeight // self.numOfRows)+marginH
        x1 = (col+1) * (self.canvasWidth // self.numOfCols)-marginW
        y1 = (row+1) * (self.canvasHeight // self.numOfRows)-marginH
        self.canvas.create_oval(x0, y0, x1, y1, fill=color, tag="circles")

    def callback(self, event):
        # clickedRow = abs((event.y // (self.canvasHeight // self.numOfRows)))
        clickedCol = event.x // (self.canvasWidth // self.numOfCols)
        desiredRow = abs(self.lastRow[clickedCol]-5)
        if (self.lastRow[clickedCol] == self.numOfRows):
            gameAlgorithm.game(self.numOfRows, self.numOfCols, self.board)
            return
        self.putCircle(desiredRow, clickedCol, self.colors[self.turn])
        indx = desiredRow * self.numOfRows + clickedCol % self.numOfCols
        print(self.board)
        print(len(self.board))
        print(indx)
        print(len(self.board))
        if (self.turn):
            self.board = self.board[:indx] + "1" + self.board[indx+1:]
        else: self.board = self.board[:indx] + "0" + self.board[indx+1:]
        print(self.board[indx])
        self.turn = not self.turn
        self.lastRow[clickedCol] += 1
        
    def create_grid(self, event=None):
        self.wScale = event.width/self.canvasWidth # Get width scalling ratio
        self.hScale = event.height/self.canvasHeight # Get height scalling ratio
        self.canvasWidth = self.canvas.winfo_width() # Get current width of canvas
        self.canvasHeight = self.canvas.winfo_height() # Get current height of canvas
        
        self.canvas.delete("grid_line") # Will only remove the grid_line

        # Creates all vertical lines at intevals of 100
        for i in range(0, self.canvasWidth, int(self.canvasWidth/self.numOfCols)):
            self.canvas.create_line([(i, 0), (i, self.canvasHeight)], tag='grid_line', fill=self.whiteColor)

        # Creates all horizontal lines at intevals of 100
        for i in range(0, self.canvasHeight, int(self.canvasHeight/self.numOfRows)):
            self.canvas.create_line([(0, i), (self.canvasWidth, i)], tag='grid_line', fill=self.whiteColor)

        # Put all places empty blacks
        self.allBlack()

root = Tk()
gui = GUI(root)
root.mainloop()