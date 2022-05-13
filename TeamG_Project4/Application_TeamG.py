"""
Application_TeamG.py
Team G's application of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import LCG_TeamG
import datetime
from tkinter import *

class PaintApp: 
    def __init__(self,root):
        self.root = root
        
        #first color set to blue
        self.color = "blue"
        
        #create new color button and canvas, bind mouse motion to function
        color_button = Button(root, text="New color", command = self.coloring ).pack()
        self.wn=Canvas(root, width=500, height=350, bg='white')
        self.wn.bind('<B1-Motion>', self.paint)
        self.wn.pack()
        
        #create color list
        self.colorList = ["red","orange","yellow","green","blue","purple","brown",
                            "green3", "tan1","slateblue2","red4","purple4",
                            "maroon","pink","palegreen","black","gray",
                            "midnightblue","maroon2","lightgoldenrod1"]

    def coloring(self):
        #pick a color from the colorList by using function PaintNumber
        self.color = self.colorList[self.PaintNumber()]
        
    def paint(self,event):
        #This function gets the x and y coordinates from event and draws an oval on the canvas
        x1, y1 = (event.x-3), (event.y-3)
        x2,y2 = (event.x+3), (event.y+3)
        self.wn.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)

    def PaintNumber(self):
        #This function will call our LCG random number algorithm
        #@returns a random number from 0-19
        today = datetime.datetime.now()
        now = today.second
        now = LCG_TeamG.LCG_TeamG(now)
        return (now%20)

 #set up root and run program
root = Tk()
root.title("Random Paint Application")
root.geometry("500x300")
app = PaintApp(root)
root.mainloop()
