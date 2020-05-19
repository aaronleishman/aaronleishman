import requests
from datetime import datetime

class Weather(object):
    def __init__(self,lati,long,api,units,addr):
        self.lati = lati
        self.long = long
        self.api = api
        self.units = units
        self.addr = addr
        self.getLiveWeather(lati,long,api,units)
        self.getForecastWeather(lati,long,api,units)

    def getLiveWeather(self,lat,lon,api,units):
        print("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api + "&lat=" + lat +"&lon=" + lon + "&" + "units=" + units)
        self.liveWeather_Url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api + "&lat=" + lat +"&lon=" + lon + "&" + "units=" + units
        self.apiLiveData = requests.get(self.liveWeather_Url).json()
        self.errorCode = self.apiLiveData['cod']
        self.lastRefresh = datetime.now()
        self.liveTemp = str(round(self.apiLiveData['main']['temp'],1)) + "F"
        self.liveFeelsLike = str(round(self.apiLiveData['main']['feels_like'],1)) + "F"
        self.liveDescription = self.apiLiveData['weather'][0]['description']
        self.liveDescriptionIcon = self.apiLiveData['weather'][0]['icon']
        self.liveHumidity = str(self.apiLiveData['main']['humidity']) + "%"
        self.livePressure = str(round((self.apiLiveData['main']['pressure']/33.8637526),1)) + "in" # divide by 33.8637526 converts milbars to inches
        self.liveWindSpeed = str(round(self.apiLiveData['wind']['speed'],1)) + "MPH"
        self.liveWindDeg = self.apiLiveData['wind']['deg']
        self.liveWindDirection = self.windDirection(self.liveWindDeg)
        self.liveSunrise = datetime.fromtimestamp(self.apiLiveData['sys']['sunrise']).strftime('%l:%M%p')
        self.liveSunset = datetime.fromtimestamp(self.apiLiveData['sys']['sunset']).strftime('%l:%M%p')

    def getForecastWeather(self,lat,lon,api,units):
        self.forecastWeather_Url = "http://api.openweathermap.org/data/2.5/forecast?" + "appid=" + api + "&lat=" + lat +"&lon=" + lon + "&" + "units=" + units
        self.apiForecastData = requests.get(self.forecastWeather_Url).json()
        self.forecastDateTime= []
        self.forecastTemp=[]
        self.forecastHumidity=[]
        self.forecastDescription=[]
        self.forecastDescIcon=[]
        self.forecastWindSpeed=[]
        self.forecastWindDeg=[]
        self.forecastWindDirection=[]
        for i in range(len(self.apiForecastData['list'])):
            self.forecastDateTime.append(datetime.fromtimestamp(self.apiForecastData['list'][i]['dt']))
            self.forecastTemp.append(str(round(self.apiForecastData['list'][i]['main']['temp'],1)))
            self.forecastHumidity.append(str(self.apiForecastData['list'][i]['main']['humidity']))
            self.forecastDescription.append(self.apiForecastData['list'][i]['weather'][0]['description'])
            self.forecastDescIcon.append(self.apiForecastData['list'][i]['weather'][0]['icon'])
            self.forecastWindSpeed.append(str(round(self.apiForecastData['list'][i]['wind']['speed'],1)))
            self.forecastWindDeg.append(self.apiForecastData['list'][i]['wind']['deg'])
            self.forecastWindDirection.append(self.windDirection(self.forecastWindDeg[i]))

    def windDirection(self,deg):
        if deg > 337.5 or deg < 22.5:
            self.liveWindDirection = 'N'
        if deg > 22.5 and deg <67.5:
            self.liveWindDirection = 'NE'
        if deg > 67.5 and deg < 112.5:
            self.liveWindDirection = 'E'
        if deg > 112.5 and deg <157.5:
            self.liveWindDirection = 'SE'
        if deg > 157.5 and deg < 202.5:
            self.liveWindDirection = 'S'
        if deg > 202.5 and deg <247.5:
            self.liveWindDirection = 'SE'
        if deg > 247.5 and deg < 292.5:
            self.liveWindDirection = 'W'
        if deg > 292.5 and deg < 337.5:
            self.liveWindDirection = 'NW'
        return self.liveWindDirection
