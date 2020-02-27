#!/usr/bin/env python3

import requests
from datetime import datetime

# Must get your own API request from Open Weather API
api_key = "1dcb94b0a7402e4276c609e0f9a910d0" # change to your API key

def getWeather(base_Url, api_Key, cityName, Units):
    complete_Url = base_Url + "appid=" + api_Key + "&q=" + cityName + "&" + Units
    api_data = requests.get(complete_Url).json()
    return api_data

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



units = "units=imperial"
currentWeather_url = "http://api.openweathermap.org/data/2.5/weather?"
forcastWeather_url = "http://api.openweathermap.org/data/2.5/forecast?"
city_name = input("Enter city name or zip: ")

Weather_data = getWeather(currentWeather_url,api_key, city_name, units)

Forecast_data = getWeather(forcastWeather_url,api_key, city_name, units)

if Weather_data['cod'] != 200:
    print('Error: ',Weather_data['cod'])
else:
    ts_now = datetime.now()
    c_temp = str(round(Weather_data['main']['temp'],1))
    c_feelsLike = str(round(Weather_data['main']['feels_like'],1))
    c_description = Weather_data['weather'][0]['description']
    c_humidity = str(Weather_data['main']['humidity'])
    c_pressure = str(round((Weather_data['main']['pressure']/33.8637526),1)) # divide by 33.8637526 converts milbars to inches
    c_windSpeed = str(round(Weather_data['wind']['speed'],1))
    c_windDeg = Weather_data['wind']['deg']
    ts_sunrise = datetime.fromtimestamp(Weather_data['sys']['sunrise'])
    ts_sunset = datetime.fromtimestamp(Weather_data['sys']['sunset'])
    t_sunrise = ts_sunrise.strftime('%l:%M%p')
    t_sunset = ts_sunset.strftime('%l:%M%p')
    print("")
    print(ts_now.strftime('%a:%m/%d'))
    print("\t",ts_now.strftime('%l:%M%p'))
    print ("\t\tTemp: " + c_temp +"F | " +
       "Feels Like: " + c_feelsLike + "F | " +
        c_description.title() + " | \n\t\t"  +
        "Wind: " + winddirection(c_windDeg) , c_windSpeed + " MPH | " +
        " Humidity: " + c_humidity + "% | "  +
        " Barometer: " + c_pressure + "in | \n\t\t" +
        "Sunrise:" + t_sunrise + " | Sunset:" + t_sunset + " |")


    print("")

    for i in range(len(Forecast_data['list'])):
        d1 = datetime.fromtimestamp(Forecast_data['list'][i]['dt'])
        f_time = d1.strftime('%l:%M%p')
        f_temp = str(round(Forecast_data['list'][i]['main']['temp'],1))
        f_humidity = str(Forecast_data['list'][i]['main']['humidity'])
        f_description = Forecast_data['list'][i]['weather'][0]['description']
        f_windSpeed = str(round(Forecast_data['list'][i]['wind']['speed'],1))
        f_windDeg = Forecast_data['list'][i]['wind']['deg']

        if i == 0:
            print(d1.strftime('%a:%m/%d'))
        else:
            d2 = datetime.fromtimestamp(Forecast_data['list'][i-1]['dt'])
            if d1.date()>d2.date():
                print(d1.strftime('%a:%m/%d'))
        print("\t" + f_time + " | " + f_temp + "F | " + f_description.title() + " | Wind: " +
              winddirection(f_windDeg)+ " " + f_windSpeed + " MPH " + " | Humidity: " +
              f_humidity + "% |")
