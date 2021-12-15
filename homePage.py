import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import main
class MyWindow:
    def __init__(self, win):
        self.bar = Frame(window, relief=RIDGE)
        self.bar.pack(side=TOP)
        self.iconPath = 'm2.jpg'  # display the background image.
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self.bar)
        self.icon_size.image = self.icon  # <== this is were we anchor the img object
        self.icon_size.configure(image=self.icon)
        self.icon_size.pack(side=LEFT)

        self.lbl1=Label(win, text='Number of rows')
        self.lbl2=Label(win, text='Number of columns')
        self.lbl3=Label(win, text='Number of depth levels')
        self.lbl1.place(x=50, y=50)
        self.lbl2.place(x=50, y=100)
        self.lbl3.place(x=50, y=150)

        self.entryText1 = tkinter.StringVar()
        self.entryText1.set(6)
        self.t1=Entry(bd=3, textvariable=self.entryText1)
        self.entryText2 = tkinter.StringVar()
        self.entryText2.set(7)
        self.t2=Entry(bd=3, textvariable=self.entryText2)
        self.entryText3 = tkinter.StringVar()
        self.entryText3.set(3)
        self.t3=Entry(bd=3, textvariable=self.entryText3)
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=100)
        self.t3.place(x=200, y=150)

        self.v0 = IntVar()
        self.v0.set(2)
        self.r1 = Radiobutton(window, text="With alpha-beta pruning", variable=self.v0, value=1)
        self.r2 = Radiobutton(window, text="Without alpha-beta pruning", variable=self.v0, value=2)
        self.r1.place(x=50, y=200)
        self.r2.place(x=210, y=200)
        #print(self.v0.get())


        self.b1 = Button(win, text='Start Game', command=self.start)
        self.b1.place(x=200, y=250)

    def start(self):
        #self.t3.delete(0, 'end')
        # if self.t1.get()!=" " and self.t1.get()!=" " :
        self.check_user_input(self.t1.get())
        self.check_user_input(self.t2.get())
        self.check_user_input(self.t3.get())
        num_row = int(self.t1.get())
        num_col = int(self.t2.get())
        num_depth = int(self.t3.get())
        bool_with = False
        if(self.v0.get() == 1):
            bool_with = True
        window.destroy()

        root = Tk()
        main.GUI(root, num_row, num_col, num_depth, bool_with)
        root.mainloop()
        # result = num1+num2
        # self.t3.insert(END, str(result + self.v0.get()))

    def check_user_input(self, input):
        try:
            # Convert it into integer
            val = int(input)
            print("Input is an integer number. Number = ", val)
        except ValueError:
            try:
                # Convert it into float
                val = float(input)
                # print("Input is a float  number. Number = ", val)
            except ValueError:
                tkinter.messagebox.showinfo("Warning", "No.. input is not a number. It's a string!")


window=Tk()
mywin=MyWindow(window)
window.title('Home Page Of Connect Four!')
window.geometry("473x414+10+10") #400x300+10+10
window.mainloop()