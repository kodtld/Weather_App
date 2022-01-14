from email.mime import image
import tkinter as tk
from tkinter import font
import requests
from requests.api import request
from urllib.request import urlopen

S_Height = 300
S_Width =  700

def format_response(got_weather):
    try:
        City_Name = got_weather['location']['name']
        City_Country = got_weather['location']['country']
        City_Condition = got_weather['current']['condition']['text']
        City_Temp = got_weather['current']['temp_c']
        City_Feels = got_weather['current']['feelslike_c']
        City_Wind = got_weather['current']['gust_kph']
    
        return f"{City_Name}, {City_Country} | {City_Condition}\nTemperature: {City_Temp} °C | Feels like: {City_Feels} °C | Wind: {City_Wind} (kph)"
        
    except:
        return "Koomikko laita oikee kaupunki"


def get_weather(entry):
    API_key = "7f68cf1250d1472a8ee143624221201"
    API_call = f"http://api.weatherapi.com/v1/current.json"
    params = {'key': API_key, 'q': entry,'alerts': "yes", 'aqi': "yes"}
    request = requests.get(API_call,params=params)
    got_weather = request.json()
    label['text'] = format_response(got_weather)
    
root = tk.Tk()
root.title("Get Weather")

canvas = tk.Canvas(root, height = S_Height, width = S_Width,bg="#8585ad")
canvas.pack()

background_image = tk.PhotoImage(file = './weather_bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

# Top Frame

frame_top = tk.Frame(root, bg = "#006680")
frame_top.place(relx = 0.1, rely = 0.1, relwidth = 0.8 ,relheight = 0.25)

button = tk.Button(frame_top, text = "Get Weather", bg = "#f2f2f2", fg = "black",font=("Nimbus Sans L",13),command= lambda: get_weather(entry.get()))
button.place(relx = 0.69, rely = 0.1, relwidth = 0.3 ,relheight = 0.8)

entry= tk.Entry(frame_top, bg= "#f2f2f2",fg="black",font=("Nimbus Sans L",13))
entry.place(relx=0.01,rely=0.1,relwidth=0.65,relheight=0.8)

# Bottom Frame

frame_bot = tk.Frame(root, bg = "#006680")
frame_bot.place(relx = 0.1, rely = 0.5, relwidth = 0.8 ,relheight = 0.4)

label = tk.Label(frame_bot, text= "",image= "", bg="#f2f2f2",font=("Nimbus Sans L",13),anchor='nw',justify='left',bd=4)
label.place(relx=0.03,rely=0.1,relwidth=0.94,relheight=0.80)

root.mainloop()