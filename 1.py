#! python3

# import de librairies
import tkinter
import random

# initialisation
window = tkinter.Tk()
window.resizable(width = False, height = False)
window.title("Game of Life 1")
window.geometry("500x500")

background = tkinter.Canvas(window, width = 500, height = 500, background="#000", bd=0, highlightthickness=0)
background.pack()

Seed = [[230, 230], [240, 230], [250, 230], [270, 230], [230, 240], [260, 250], [270, 250], [240, 260], [250, 260], [270, 260], [230, 270], [250, 270], [270, 270]]

class Cell:
    def __init__(self, x, y):
        self.object = background.create_rectangle(x, y, x+10, y+10, fill="#000", outline="")
        self.alive = False;
        if ([x, y] in Seed):
            background.itemconfig(self.object, fill="#FFF")
            self.alive = True

    def born(self):
        background.itemconfig(self.object, fill="#FFF")
        self.alive = True

    def die(self):
        background.itemconfig(self.object, fill="#000")
        self.alive = False

def motion():
    for x in range(0, 500, 10):
        for y in range(0, 500, 10):
            neightbor = 0
            if (Cells['%i,%i'%(x,y)].alive == True):
                for a in range(max(x-10, 0), min(x+20, 500), 10):
                    for b in range(max(y-10, 0), min(y+20, 500), 10):
                        if (Cells['%i,%i'%(a,b)].alive == True):
                            neightbor += 1
                if (neightbor < 3 or neightbor > 4):
                    Cells['%i,%i'%(x,y)].die()
            else:
                for a in range(max(x-10, 0), min(x+20, 500), 10):
                    for b in range(max(y-10, 0), min(y+20, 500), 10):
                        if (Cells['%i,%i'%(a,b)].alive == True):
                            neightbor += 1
                if (neightbor == 3):
                    Cells['%i,%i'%(x,y)].born()
    window.after(100, motion)

Cells = {'%i,%i'%(x,y):Cell(x, y) for x in range(0, 500, 10) for y in range(0, 500, 10)}

motion()
window.mainloop()
