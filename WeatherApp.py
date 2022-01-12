import tkinter as tk
from tkinter import font
import requests
from requests.api import request
from requests.models import Response



S_Height = 700
S_Width =  800



#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API key}


def format_response(got_weather):
    try:
        City_Name = got_weather['location']['name']
        City_Country = got_weather['location']['country']
        City_Condition = got_weather['current']['condition']['text']
        City_Temp = got_weather['current']['temp_c']
        City_Feels = got_weather['current']['feelslike_c']
        City_Wind = got_weather['current']['gust_kph']

        return f"{City_Name}, {City_Country} \n {City_Condition} \n  Temperature: {City_Temp}°C Feels like: {City_Feels}°C\n Wind: {City_Wind} (kph)"

    except:
        return "Koomikko laita oikee kaupunki"
def get_weather(entry):
    API_key = "7f68cf1250d1472a8ee143624221201"
    API_call = f"http://api.weatherapi.com/v1/current.json"
    params = {'key': API_key, 'q': entry,'alerts': "yes", 'aqi': "yes"}
    request = requests.get(API_call,params=params)
    got_weather = request.json()

    label['text'] = format_response(got_weather)
    

{'location': {'name': 'Helsinki', 'region': 'Southern Finland', 'country': 'Finland', 'lat': 60.18, 'lon': 24.93, 'tz_id': 'Europe/Helsinki', 'localtime_epoch': 1642001263, 'localtime': '2022-01-12 17:27'}, 'current': {'last_updated_epoch': 1642000500, 'last_updated': '2022-01-12 17:15', 'temp_c': 1.0, 'temp_f': 33.8, 'is_day': 0, 'condition': {'text': 'Mist', 'icon': '//cdn.weatherapi.com/weather/64x64/night/143.png', 'code': 1030}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 210, 'wind_dir': 'SSW', 'pressure_mb': 
1016.0, 'pressure_in': 30.0, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 100, 'cloud': 100, 'feelslike_c': -4.7, 'feelslike_f': 23.6, 'vis_km': 1.8, 'vis_miles': 1.0, 'uv': 1.0, 'gust_mph': 22.1, 'gust_kph': 35.6, 'air_quality': {'co': 310.3999938964844, 'no2': 6.300000190734863, 'o3': 48.599998474121094, 'so2': 2.0999999046325684, 'pm2_5': 4.099999904632568, 'pm10': 5.800000190734863, 'us-epa-index': 1, 'gb-defra-index': 1}}}    
    


root = tk.Tk()

canvas = tk.Canvas(root, height = S_Height, width = S_Width,bg="#8585ad")
canvas.pack()

background_image = tk.PhotoImage(file = './weather_bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

# Top Frame

frame_top = tk.Frame(root, bg = "#006680")
frame_top.place(relx = 0.1, rely = 0.1, relwidth = 0.8 ,relheight = 0.1)

button = tk.Button(frame_top, text = "Get Weather", bg = "#f2f2f2", fg = "black",font=("Nimbus Sans L",13),command= lambda: get_weather(entry.get()))
button.place(relx = 0.69, rely = 0.1, relwidth = 0.3 ,relheight = 0.8)

entry= tk.Entry(frame_top, bg= "#f2f2f2",fg="black",font=("Nimbus Sans L",13))
entry.place(relx=0.01,rely=0.1,relwidth=0.65,relheight=0.8)

# Bottom Frame

frame_bot = tk.Frame(root, bg = "#006680")
frame_bot.place(relx = 0.1, rely = 0.3, relwidth = 0.8 ,relheight = 0.6)

label = tk.Label(frame_bot, text= "Label is this", bg="#f2f2f2",font=("Nimbus Sans L",13))
label.place(relx=0.015,rely=0.02,relwidth=0.97,relheight=0.96)



root.mainloop()