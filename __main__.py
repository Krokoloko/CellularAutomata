import tkinter as tk
from Cell import Cell
from Celluler_Automaton import CA

import random as rnd

def Rule(cell,neighbours):
    alive = 0
    for nb in neighbours:
        if nb.state == 1:
            alive += 1
    if cell.state == 1:  
        if alive == 2:
            cell.state = 0
        if alive == 1:
            cell.state = 0
        if alive == 0:
            cell.state = 1
    else:
        if alive == 2:
            cell.state = 1
        if alive == 1:
            cell.state = 0
        if alive == 0:
            cell.state = 1
    return cell


canvas = [int(1700),int(1000)]
adjecent = [-1,1]
master = tk.Tk()
length = canvas[0]/8
grid = [Cell.Cell(int(rnd.random()*2),adjecent) for x in range(int(length))]
ca = CA.CA(grid,adjecent,Rule)
canv = tk.Canvas(master, width=canvas[0], height=canvas[1])
canv.pack()

def Main():
    
    height = 8
    cellWidth = int(canvas[0]/int(length))
    while height <= canvas[1]:
        for i,x in enumerate(ca.newgen):
            color = ""
            if x.state == 1:
                color = "#ff00ff"
            else:
                color = "#000000"
            canv.create_rectangle(i*cellWidth,canvas[1]-height,i*cellWidth+8,canvas[1]-height+8, fill=color)
        height += 8
        ca.nextGen()
        

if __name__ == "__main__":
    Main()
