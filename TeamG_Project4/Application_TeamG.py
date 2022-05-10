"""
Application_TeamG.py
Team 5's application of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import LCG_TeamG
import datetime

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

    
       