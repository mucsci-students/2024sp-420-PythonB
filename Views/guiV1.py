from tkinter import *

master = Tk()
w = Canvas(master, width=400, height=600)
w.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width,y)
mainloop()