import tkinter as tk
from tkinter.constants import LEFT, RIGHT

S_Height = 700
S_Width =  800

root = tk.Tk()

canvas = tk.Canvas(root, height = S_Height, width = S_Width,bg="#8585ad")
canvas.pack()

background_image = tk.PhotoImage(file = './weather_bg.jpg')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)

# Top Frame

frame_top = tk.Frame(root, bg = "#ccf2ff")
frame_top.place(relx = 0.1, rely = 0.1, relwidth = 0.8 ,relheight = 0.1)

button = tk.Button(frame_top, text = "Nappi", bg = "#f2f2f2", fg = "black")
button.place(relx = 0.69, rely = 0.1, relwidth = 0.3 ,relheight = 0.8)

entry= tk.Entry(frame_top, bg= "#f2f2f2",fg="black")
entry.place(relx=0.01,rely=0.1,relwidth=0.65,relheight=0.8)

# Bottom Frame

frame_bot = tk.Frame(root, bg = "#ccf2ff")
frame_bot.place(relx = 0.1, rely = 0.3, relwidth = 0.8 ,relheight = 0.6)

label = tk.Label(frame_bot, text= "Label is this", bg="#f2f2f2")
label.place(relx=0.015,rely=0.02,relwidth=0.97,relheight=0.96)



root.mainloop()