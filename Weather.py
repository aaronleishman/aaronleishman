#!/usr/bin/env python3

import requests
from datetime import datetime

def winddirection(deg):
    if deg > 337.5 or deg < 22.5:
        w_direction = 'N'
    if deg > 22.5 and deg <67.5:
        w_direction = 'NE'
    if deg > 67.5 and deg < 112.5:
        w_direction = 'E'
    if deg > 112.5 and deg <157.5:
        w_direction = 'SE'
    if deg > 157.5 and deg < 202.5:
        w_direction = 'S'
    if deg > 202.5 and deg <247.5:
        w_direction = 'SE'
    if deg > 247.5 and deg < 292.5:
        w_direction = 'W'
    if deg > 292.5 and deg < 337.5:
        w_direction = 'NW'
    return w_direction

api_key = "1dcb94b0a7402e4276c609e0f9a910d0"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
units = "units=imperial" 
city_name = "52641"

# http://api.openweathermap.org/data/2.5/weather?appid=1dcb94b0a7402e4276c609e0f9a910d0&q=52641&units=imperial
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&" + units 
response_data = requests.get(complete_url).json()


c_temp = str(round(response_data['main']['temp'],1))
c_feelsLike = str(round(response_data['main']['feels_like'],1))
c_description = response_data['weather'][0]['description']
c_humidity = str(response_data['main']['humidity'])
c_pressure = str(round((response_data['main']['pressure']/33.8637526),1)) # divide by 33.8637526 converts milbars to inches
c_windSpeed = str(round(response_data['wind']['speed'],1))
c_windDeg = response_data['wind']['deg']

#sunrise and sunset
ts_sunrise = datetime.fromtimestamp(response_data['sys']['sunrise'])
ts_sunset = datetime.fromtimestamp(response_data['sys']['sunset'])

t_sunrise = ts_sunrise.strftime('%l:%M:%p')
t_sunset = ts_sunset.strftime('%l:%M:%p')

print ("Currently: " + c_temp +"F | " +
       "Feels Like: " + c_feelsLike + "F | " +
        c_description + " | \n"  +
        "Wind: " + winddirection(c_windDeg) , c_windSpeed + " MPH | " +
        " Humidity: " + c_humidity + "% | "  +
        " Barometer: " + c_pressure + "in | \n" +
        "Sunrise:" + t_sunrise + " | Sunset:" + t_sunset + " |")



