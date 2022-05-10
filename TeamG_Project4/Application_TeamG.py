"""
Application_TeamG.py
Team 5's application of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import LCG_TeamG
import datetime
from tkinter import *

#root = Tk()
#root.title("Random Paint Application")
#root.geometry("500x300")


class PaintApp: 

    def __init__(self,root):
        self.root = root
        self.color = "blue"
        color_button = Button(root, text="New color", command = self.coloring ).pack()
        self.wn=Canvas(root, width=500, height=350, bg='white')
        self.wn.bind('<B1-Motion>', self.paint)
        self.wn.bind("<ButtonPress-1>", self.coloring)
        self.wn.pack()

    def coloring(self):
        self.color = "red"


    def paint(self,event):
        x1, y1 = (event.x-3), (event.y-3)
        x2,y2 = (event.x+3), (event.y+3)
        self.wn.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)

    

# create canvas
#wn=Canvas(root, width=500, height=350, bg='white')

#button_frame = Frame(root, width = 400, height = 50)
#button_frame.grid(row = 2, column = 1)

#color_button = Button(root, text="New color", command = coloring).pack()
#color_button.grid(row=1, column=1)

# bind mouse event with canvas(wn)
#wn.bind('<B1-Motion>', self.paint)
#wn.bind("<ButtonPress-1>", color)
#wn.pack()
root = Tk()
root.title("Random Paint Application")
root.geometry("500x300")
app = PaintApp(root)
root.mainloop()


def PaintNumber(now):
        now = LCG_TeamG.LCG_TeamG(now)
        return (now%28)

def PaintNumberList():
    today = datetime.datetime.now()
    now = today.second
    numbers = []
    for i in range (4):
        now = LCG_TeamG.LCG_TeamG(now)
        numbers.append(now)
        i+=1
    return numbers
        
def ColoringBook(paintnumbers):
        print("Open your coloring book by using this link: https://jspaint.app/#local:27c2c8d383dbb")
        num1 = PaintNumber(paintnumbers[0])
        print("Your sky color is color number ", num1)
        num2 = PaintNumber(paintnumbers[1])
        print("Your ground color is color number ", num2)
        num3 = PaintNumber(paintnumbers[2])
        print("Your sun color is color number ", num3)
        num4 = PaintNumber(paintnumbers[3])
        print("Your tree color is color number ", num4)

if __name__ == "__main__":
    paintnumbers = PaintNumberList()
    ColoringBook(paintnumbers)

    
       