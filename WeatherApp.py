import tkinter as tk
from tkinter.constants import LEFT, RIGHT

S_Height = 700
S_Width =  800

root = tk.Tk()

canvas = tk.Canvas(root, height = S_Height, width = S_Width)
canvas.pack()

frame = tk.Frame(root, bg = "#ccf2ff")
frame.place(relheight = 1, relwidth= 1)

button = tk.Button(frame, text = "Nappi", bg = "#f0f0f5", fg = "black")
button.pack(side=LEFT)

label = tk.Label(frame, text= "Label is this", bg="red")
label.pack(side=RIGHT)

entry= tk.Entry(frame, bg= "green")
entry.pack(side=RIGHT)

root.mainloop()