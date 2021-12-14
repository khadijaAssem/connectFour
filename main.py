from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox
import gameAlgorithm
import algorithms

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

    canvasWidth = 570
    canvasHeight = 500
    wScale = 1
    hScale = 1

    numOfRows = 6
    numOfCols = 7
    lastRow = '0'*numOfCols

    oponentSign = '1'
    agentSign = '0'
    defaultSign = '2'
    signs = {True: '1', False: '0'}
    colors = {True: greenColor, False: redColor}
    
    # 0 for human(red) 1 for computer(green)
    turn = True

    def __init__(self, master, numOfRows, numOfCols, k_levels, withPruning):
        self.numOfRows = numOfRows
        self.numOfCols = numOfCols
        self.k_levels = k_levels
        self.withPruning = withPruning
        self.board = self.defaultSign*(self.numOfRows * self.numOfCols) #[[-1]*self.numOfCols for i in range(self.numOfRows)]
        
        self.master = master  # the root object.
        master.title("Connect four")
        self.canvas = Canvas(master, width=self.canvasWidth, height=self.canvasHeight, background=self.backgroundColor, highlightthickness=0)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.create_grid)
        self.heuristic = gameAlgorithm.game(self.numOfRows, self.numOfCols, self.oponentSign, self.agentSign, self.defaultSign)
        self.miniMax = algorithms.Minimax_Class(self.numOfRows, self.numOfCols, k_levels, self.oponentSign, self.agentSign, self.defaultSign)
    
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
        desiredRow = abs(int(self.lastRow[clickedCol])-self.numOfRows+1)
        if (self.turn):
            if (self.playStep(desiredRow ,clickedCol)):
                # self.heuristic.getHeuristic(self.board, not self.turn)
                # return
                row, col = self.miniMax.getStep([(self.board, (-1, -1), self.lastRow)])
                self.playStep(row, col)


    def playStep(self, row, col):
        if (int(self.lastRow[col]) == self.numOfRows):
            print(self.heuristic.getScore(self.board))
            return False
        self.putCircle(row, col, self.colors[self.turn]) # put elzorar fl GUI
        indx = row * self.numOfCols + col # calculate index in string
        self.board = self.board[:indx] + self.signs[self.turn] + self.board[indx+1:] # do actual change in string
        self.turn = not self.turn # switch turn
        self.lastRow = self.lastRow[0:col] + str(int(self.lastRow[col]) + 1) + self.lastRow[col + 1:] # update last available row in column
        return True
        
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

# root = Tk()
# gui = GUI(root)
# root.mainloop()
