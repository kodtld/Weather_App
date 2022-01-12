import tkinter as tk
import requests
from requests.models import Response

S_Height = 700
S_Width =  800



#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API key}



def get_weather(entry):
    API_key = "7f68cf1250d1472a8ee143624221201"
    API_call = f"http://api.weatherapi.com/v1/current.json"
    params = {'key': API_key, 'q': entry,'alerts': "no", 'aqi': "no"}
    response = requests.get(API_call,params=params)
    print(response.json())

root = tk.Tk()

canvas = tk.Canvas(root, height = S_Height, width = S_Width,bg="#8585ad")
canvas.pack()

background_image = tk.PhotoImage(file = './weather_bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

# Top Frame

frame_top = tk.Frame(root, bg = "#006680")
frame_top.place(relx = 0.1, rely = 0.1, relwidth = 0.8 ,relheight = 0.1)

button = tk.Button(frame_top, text = "Get Weather", bg = "#f2f2f2", fg = "black",command= lambda: get_weather(entry.get()))
button.place(relx = 0.69, rely = 0.1, relwidth = 0.3 ,relheight = 0.8)

entry= tk.Entry(frame_top, bg= "#f2f2f2",fg="black")
entry.place(relx=0.01,rely=0.1,relwidth=0.65,relheight=0.8)

# Bottom Frame

frame_bot = tk.Frame(root, bg = "#006680")
frame_bot.place(relx = 0.1, rely = 0.3, relwidth = 0.8 ,relheight = 0.6)

label = tk.Label(frame_bot, text= "Label is this", bg="#f2f2f2")
label.place(relx=0.015,rely=0.02,relwidth=0.97,relheight=0.96)



root.mainloop()