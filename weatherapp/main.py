import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from PIL import Image,ImageTk
import ttkbootstrap
from datetime import datetime
import pytz
import datetime


def get_weather(city):
    API_key = "d9b5e1e2e452bd8a28a631ffd90e2f2a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']  # Corrected key name
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']  # Corrected key name
    city_name = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"  # Removed extra 'd'
    return (icon_url, temperature, description, city_name, country)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city_name, country = result
    location.configure(text=f"{city_name}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image=image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temp.configure(text=f"Temperature: {temperature:.2f}°C")
    describe_label.configure(text=f"Description: {description}")



root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("900x900")

#





#end
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")  # Corrected font specification
city_entry.pack(pady=10)

# Button widget
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location = tk.Label(root, font="Helvetica, 25")
location.pack(pady=20)

icon_label = tk.Label(root, font="Helvetica, 20")
icon_label.pack()

temp = tk.Label(root, font="Helvetica, 20")
temp.pack()

describe_label = tk.Label(root, font="Helvetica, 20")
describe_label.pack()

root.mainloop()
