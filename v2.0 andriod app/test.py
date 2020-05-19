from weather import Weather
from datetime import datetime

#Need to import files zip & api
zip = open("zip.txt", "r")
api = open("api.txt", "r")
units = open("units.txt", "r")

# file.read() includes EOF character in string, Need to remove it
zipcode = zip.read()[0:len(zip.read())-1]
apikey = api.read()[0:len(api.read())-1]
um = units.read()[0:len(units.read())-1]


aaron = Weather(zipcode,apikey,um)
print(aaron.liveTemp)
print(aaron.liveSunrise)
print(aaron.liveWindDeg)
print(aaron.liveWindDirection)
print(type(aaron.forecastDateTime[0]))
print(aaron.forecastTemp[0])
print(aaron.forecastHumidity[0])
print(aaron.forecastDescription[0])
print(aaron.forecastWindSpeed[0])
print(aaron.forecastWindDeg[0])
print(aaron.forecastWindDirection[0])
#print(datetime.fromtimestamp(aaron.forecastDateTime[0]))
