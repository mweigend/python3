#----------------------------------------------------
# Dateiname:  weather.py 
# 
# Python 3
# Kap. 26
# Michael Weigend 08.06. 2019
#----------------------------------------------------
import json
from urllib.request import urlopen
ID = "365732826eb5f25bb6da21b0f4355337"             #1
URL = "http://api.openweathermap.org/data/2.5/weather?zip={},de&APPID={}"
REPORT = """
Wetterbericht für {}:
Temperatur: {:.1f} °C
Lufdruck: {:.1f} bar
""" 
print("Geben Sie die Postleitzahl einer Stadt in Deutschland ein.")
city = input("PLZ: ")
while city:                                         #3
    try:
        f = urlopen(URL.format(city, ID))               #4
        data = json.load(f)                         #5
        name_city = data["name"]
        temp = data["main"]["temp"]-273.15          #6
        pressure = data["main"]["pressure"]
        print(REPORT.format(name_city, temp, pressure)) #7
    except:
        print("Fehler. Vielleicht war die Postleitzahl ungültig.")    
    city = input("PLZ: ")
print("Auf Wiedersehen!")
