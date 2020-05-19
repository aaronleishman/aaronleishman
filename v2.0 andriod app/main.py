from kivymd.app import MDApp
from weather import Weather
from kivy.core.window import Window
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
from datetime import datetime
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
    Window.size = (400, 600)
    with open("lat.txt", "r") as lat_coord:
        lat_coord = lat_coord.read()
    with open("lon.txt", "r") as lon_coord:
        lon_coord = lon_coord.read()
    with open("api.txt", "r") as apikey:
        apikey = apikey.read()
    with open("units.txt", "r") as um:
        um = um.read()
    with open("addr.txt", "r") as addr:
        addr = addr.read()


    w = Weather(lat_coord,lon_coord,apikey,um,addr)


    def on_start(self):
        self.theme_cls.primary_palette = 'Blue'
        self.search_menu = SearchPopupMenu()
        # print(self.theme_cls.primary_palette)
        # print(self.root.ids)
        # print(self.w.forecastDescIcon[0])
        # print(len(self.w.apiForecastData['list']))

        # print(self.root.ids.outlook)

    def updateTemp(self):
        # get new lat lon

        # send lat and lon to Weather object

        # assign text values to the new Weather object
        self.root.ids.l1.text = self.w.addr
        self.root.ids.l1.secondary_text = 'lat: ' + self.w.lati + ' lon: ' + self.w.long
        self.root.ids.l2.text = self.w.liveDescription.title()
        self.root.ids.l3.text = self.w.liveTemp + '  |  Feels: ' + self.w.liveFeelsLike
        self.root.ids.l4.text = 'Wind: ' + self.w.liveWindDirection + " " + self.w.liveWindSpeed
        self.root.ids.l5.text = 'Humidity: ' + self.w.liveHumidity
        self.root.ids.l6.text = 'Barometer: ' + self.w.livePressure
        self.root.ids.l7.text = 'Sunrise: ' + self.w.liveSunrise
        self.root.ids.l8.text = 'Sunset: ' + self.w.liveSunset
        self.root.ids.l9.text = 'As of: ' + self.w.lastRefresh.strftime('%a: %m/%d%l:%M%p')

        self.root.ids.f00.text = self.w.addr
        self.root.ids.f00.secondary_text = 'lat: ' + self.w.lati + ' lon: ' + self.w.long
        self.root.ids.f0.text = str(self.w.forecastTemp[0]) + 'F' + ' ' +  self.w.forecastDescription[0].title()
        self.root.ids.f0.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[0]) + ' ' + str(self.w.forecastWindSpeed[0]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[0]) + "%"
        self.root.ids.f0.tertiary_text = self.w.forecastDateTime[0].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f0icon.source = 'icons/' + str(self.w.forecastDescIcon[0]) + '.png'

        self.root.ids.f1.text = str(self.w.forecastTemp[1]) + 'F' + ' ' +  self.w.forecastDescription[1].title()
        self.root.ids.f1.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[1]) + ' ' + str(self.w.forecastWindSpeed[1]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[1]) + "%"
        self.root.ids.f1.tertiary_text = self.w.forecastDateTime[1].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f1icon.source = 'icons/' + str(self.w.forecastDescIcon[1]) + '.png'

        self.root.ids.f2.text = str(self.w.forecastTemp[2]) + 'F' + ' ' +  self.w.forecastDescription[2].title()
        self.root.ids.f2.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[2]) + ' ' + str(self.w.forecastWindSpeed[2]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[2]) + "%"
        self.root.ids.f2.tertiary_text = self.w.forecastDateTime[2].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f2icon.source = 'icons/' + str(self.w.forecastDescIcon[2]) + '.png'

        self.root.ids.f3.text = str(self.w.forecastTemp[3]) + 'F' + ' ' +  self.w.forecastDescription[3].title()
        self.root.ids.f3.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[3]) + ' ' + str(self.w.forecastWindSpeed[3]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[3]) + "%"
        self.root.ids.f3.tertiary_text = self.w.forecastDateTime[3].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f3icon.source = 'icons/' + str(self.w.forecastDescIcon[3]) + '.png'

        self.root.ids.f4.text = str(self.w.forecastTemp[4]) + 'F' + ' ' +  self.w.forecastDescription[4].title()
        self.root.ids.f4.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[4]) + ' ' + str(self.w.forecastWindSpeed[4]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[4]) + "%"
        self.root.ids.f4.tertiary_text = self.w.forecastDateTime[4].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f4icon.source = 'icons/' + str(self.w.forecastDescIcon[4]) + '.png'

        self.root.ids.f5.text = str(self.w.forecastTemp[5]) + 'F' + ' ' +  self.w.forecastDescription[5].title()
        self.root.ids.f5.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[5]) + ' ' + str(self.w.forecastWindSpeed[5]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[5]) + "%"
        self.root.ids.f5.tertiary_text = self.w.forecastDateTime[5].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f5icon.source = 'icons/' + str(self.w.forecastDescIcon[5]) + '.png'

        self.root.ids.f6.text = str(self.w.forecastTemp[6]) + 'F' + ' ' +  self.w.forecastDescription[6].title()
        self.root.ids.f6.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[6]) + ' ' + str(self.w.forecastWindSpeed[6]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[6]) + "%"
        self.root.ids.f6.tertiary_text = self.w.forecastDateTime[6].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f6icon.source = 'icons/' + str(self.w.forecastDescIcon[6]) + '.png'

        self.root.ids.f7.text = str(self.w.forecastTemp[7]) + 'F' + ' ' +  self.w.forecastDescription[7].title()
        self.root.ids.f7.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[7]) + ' ' + str(self.w.forecastWindSpeed[7]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[7]) + "%"
        self.root.ids.f7.tertiary_text = self.w.forecastDateTime[7].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f7icon.source = 'icons/' + str(self.w.forecastDescIcon[7]) + '.png'

        self.root.ids.f8.text = str(self.w.forecastTemp[8]) + 'F' + ' ' +  self.w.forecastDescription[8].title()
        self.root.ids.f8.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[8]) + ' ' + str(self.w.forecastWindSpeed[8]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[8]) + "%"
        self.root.ids.f8.tertiary_text = self.w.forecastDateTime[8].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f8icon.source = 'icons/' + str(self.w.forecastDescIcon[8]) + '.png'

        self.root.ids.f9.text = str(self.w.forecastTemp[9]) + 'F' + ' ' +  self.w.forecastDescription[9].title()
        self.root.ids.f9.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[9]) + ' ' + str(self.w.forecastWindSpeed[9]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[9]) + "%"
        self.root.ids.f9.tertiary_text = self.w.forecastDateTime[9].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f9icon.source = 'icons/' + str(self.w.forecastDescIcon[9]) + '.png'

        self.root.ids.f10.text = str(self.w.forecastTemp[10]) + 'F' + ' ' +  self.w.forecastDescription[10].title()
        self.root.ids.f10.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[10]) + ' ' + str(self.w.forecastWindSpeed[10]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[10]) + "%"
        self.root.ids.f10.tertiary_text = self.w.forecastDateTime[10].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f10icon.source = 'icons/' + str(self.w.forecastDescIcon[10]) + '.png'

        self.root.ids.f11.text = str(self.w.forecastTemp[11]) + 'F' + ' ' +  self.w.forecastDescription[11].title()
        self.root.ids.f11.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[11]) + ' ' + str(self.w.forecastWindSpeed[11]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[11]) + "%"
        self.root.ids.f11.tertiary_text = self.w.forecastDateTime[11].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f11icon.source = 'icons/' + str(self.w.forecastDescIcon[11]) + '.png'

        self.root.ids.f12.text = str(self.w.forecastTemp[12]) + 'F' + ' ' +  self.w.forecastDescription[12].title()
        self.root.ids.f12.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[12]) + ' ' + str(self.w.forecastWindSpeed[12]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[12]) + "%"
        self.root.ids.f12.tertiary_text = self.w.forecastDateTime[12].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f12icon.source = 'icons/' + str(self.w.forecastDescIcon[12]) + '.png'

        self.root.ids.f13.text = str(self.w.forecastTemp[13]) + 'F' + ' ' +  self.w.forecastDescription[13].title()
        self.root.ids.f13.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[13]) + ' ' + str(self.w.forecastWindSpeed[13]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[13]) + "%"
        self.root.ids.f13.tertiary_text = self.w.forecastDateTime[13].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f13icon.source = 'icons/' + str(self.w.forecastDescIcon[13]) + '.png'

        self.root.ids.f14.text = str(self.w.forecastTemp[14]) + 'F' + ' ' +  self.w.forecastDescription[14].title()
        self.root.ids.f14.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[14]) + ' ' + str(self.w.forecastWindSpeed[14]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[14]) + "%"
        self.root.ids.f14.tertiary_text = self.w.forecastDateTime[14].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f14icon.source = 'icons/' + str(self.w.forecastDescIcon[14]) + '.png'

        self.root.ids.f15.text = str(self.w.forecastTemp[15]) + 'F' + ' ' +  self.w.forecastDescription[15].title()
        self.root.ids.f15.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[15]) + ' ' + str(self.w.forecastWindSpeed[15]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[15]) + "%"
        self.root.ids.f15.tertiary_text = self.w.forecastDateTime[15].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f15icon.source = 'icons/' + str(self.w.forecastDescIcon[15]) + '.png'

        self.root.ids.f16.text = str(self.w.forecastTemp[16]) + 'F' + ' ' +  self.w.forecastDescription[16].title()
        self.root.ids.f16.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[16]) + ' ' + str(self.w.forecastWindSpeed[16]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[16]) + "%"
        self.root.ids.f16.tertiary_text = self.w.forecastDateTime[16].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f16icon.source = 'icons/' + str(self.w.forecastDescIcon[16]) + '.png'

        self.root.ids.f17.text = str(self.w.forecastTemp[17]) + 'F' + ' ' +  self.w.forecastDescription[17].title()
        self.root.ids.f17.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[17]) + ' ' + str(self.w.forecastWindSpeed[17]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[17]) + "%"
        self.root.ids.f17.tertiary_text = self.w.forecastDateTime[17].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f17icon.source = 'icons/' + str(self.w.forecastDescIcon[17]) + '.png'

        self.root.ids.f18.text = str(self.w.forecastTemp[18]) + 'F' + ' ' +  self.w.forecastDescription[18].title()
        self.root.ids.f18.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[18]) + ' ' + str(self.w.forecastWindSpeed[18]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[18]) + "%"
        self.root.ids.f18.tertiary_text = self.w.forecastDateTime[18].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f18icon.source = 'icons/' + str(self.w.forecastDescIcon[18]) + '.png'

        self.root.ids.f19.text = str(self.w.forecastTemp[19]) + 'F' + ' ' +  self.w.forecastDescription[19].title()
        self.root.ids.f19.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[19]) + ' ' + str(self.w.forecastWindSpeed[19]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[19]) + "%"
        self.root.ids.f19.tertiary_text = self.w.forecastDateTime[19].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f19icon.source = 'icons/' + str(self.w.forecastDescIcon[19]) + '.png'

        self.root.ids.f20.text = str(self.w.forecastTemp[20]) + 'F' + ' ' +  self.w.forecastDescription[20].title()
        self.root.ids.f20.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[20]) + ' ' + str(self.w.forecastWindSpeed[20]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[20]) + "%"
        self.root.ids.f20.tertiary_text = self.w.forecastDateTime[20].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f20icon.source = 'icons/' + str(self.w.forecastDescIcon[20]) + '.png'

        self.root.ids.f21.text = str(self.w.forecastTemp[21]) + 'F' + ' ' +  self.w.forecastDescription[21].title()
        self.root.ids.f21.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[21]) + ' ' + str(self.w.forecastWindSpeed[21]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[21]) + "%"
        self.root.ids.f21.tertiary_text = self.w.forecastDateTime[21].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f21icon.source = 'icons/' + str(self.w.forecastDescIcon[21]) + '.png'

        self.root.ids.f22.text = str(self.w.forecastTemp[22]) + 'F' + ' ' +  self.w.forecastDescription[22].title()
        self.root.ids.f22.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[22]) + ' ' + str(self.w.forecastWindSpeed[22]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[22]) + "%"
        self.root.ids.f22.tertiary_text = self.w.forecastDateTime[22].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f22icon.source = 'icons/' + str(self.w.forecastDescIcon[22]) + '.png'

        self.root.ids.f23.text = str(self.w.forecastTemp[23]) + 'F' + ' ' +  self.w.forecastDescription[23].title()
        self.root.ids.f23.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[23]) + ' ' + str(self.w.forecastWindSpeed[23]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[23]) + "%"
        self.root.ids.f23.tertiary_text = self.w.forecastDateTime[23].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f23icon.source = 'icons/' + str(self.w.forecastDescIcon[23]) + '.png'

        self.root.ids.f24.text = str(self.w.forecastTemp[24]) + 'F' + ' ' +  self.w.forecastDescription[24].title()
        self.root.ids.f24.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[24]) + ' ' + str(self.w.forecastWindSpeed[24]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[24]) + "%"
        self.root.ids.f24.tertiary_text = self.w.forecastDateTime[24].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f24icon.source = 'icons/' + str(self.w.forecastDescIcon[24]) + '.png'

        self.root.ids.f25.text = str(self.w.forecastTemp[25]) + 'F' + ' ' +  self.w.forecastDescription[25].title()
        self.root.ids.f25.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[25]) + ' ' + str(self.w.forecastWindSpeed[25]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[25]) + "%"
        self.root.ids.f25.tertiary_text = self.w.forecastDateTime[25].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f25icon.source = 'icons/' + str(self.w.forecastDescIcon[25]) + '.png'

        self.root.ids.f26.text = str(self.w.forecastTemp[26]) + 'F' + ' ' +  self.w.forecastDescription[26].title()
        self.root.ids.f26.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[26]) + ' ' + str(self.w.forecastWindSpeed[26]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[26]) + "%"
        self.root.ids.f26.tertiary_text = self.w.forecastDateTime[26].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f26icon.source = 'icons/' + str(self.w.forecastDescIcon[26]) + '.png'

        self.root.ids.f27.text = str(self.w.forecastTemp[27]) + 'F' + ' ' +  self.w.forecastDescription[27].title()
        self.root.ids.f27.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[27]) + ' ' + str(self.w.forecastWindSpeed[27]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[27]) + "%"
        self.root.ids.f27.tertiary_text = self.w.forecastDateTime[27].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f27icon.source = 'icons/' + str(self.w.forecastDescIcon[27]) + '.png'

        self.root.ids.f28.text = str(self.w.forecastTemp[28]) + 'F' + ' ' +  self.w.forecastDescription[28].title()
        self.root.ids.f28.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[28]) + ' ' + str(self.w.forecastWindSpeed[28]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[28]) + "%"
        self.root.ids.f28.tertiary_text = self.w.forecastDateTime[28].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f28icon.source = 'icons/' + str(self.w.forecastDescIcon[28]) + '.png'

        self.root.ids.f29.text = str(self.w.forecastTemp[29]) + 'F' + ' ' +  self.w.forecastDescription[29].title()
        self.root.ids.f29.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[29]) + ' ' + str(self.w.forecastWindSpeed[29]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[29]) + "%"
        self.root.ids.f29.tertiary_text = self.w.forecastDateTime[29].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f29icon.source = 'icons/' + str(self.w.forecastDescIcon[29]) + '.png'

        self.root.ids.f30.text = str(self.w.forecastTemp[30]) + 'F' + ' ' +  self.w.forecastDescription[30].title()
        self.root.ids.f30.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[30]) + ' ' + str(self.w.forecastWindSpeed[30]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[30]) + "%"
        self.root.ids.f30.tertiary_text = self.w.forecastDateTime[30].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f30icon.source = 'icons/' + str(self.w.forecastDescIcon[30]) + '.png'

        self.root.ids.f31.text = str(self.w.forecastTemp[31]) + 'F' + ' ' +  self.w.forecastDescription[31].title()
        self.root.ids.f31.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[31]) + ' ' + str(self.w.forecastWindSpeed[31]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[31]) + "%"
        self.root.ids.f31.tertiary_text = self.w.forecastDateTime[31].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f31icon.source = 'icons/' + str(self.w.forecastDescIcon[31]) + '.png'

        self.root.ids.f32.text = str(self.w.forecastTemp[32]) + 'F' + ' ' +  self.w.forecastDescription[32].title()
        self.root.ids.f32.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[32]) + ' ' + str(self.w.forecastWindSpeed[32]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[32]) + "%"
        self.root.ids.f32.tertiary_text = self.w.forecastDateTime[32].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f32icon.source = 'icons/' + str(self.w.forecastDescIcon[32]) + '.png'

        self.root.ids.f33.text = str(self.w.forecastTemp[33]) + 'F' + ' ' +  self.w.forecastDescription[33].title()
        self.root.ids.f33.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[33]) + ' ' + str(self.w.forecastWindSpeed[33]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[33]) + "%"
        self.root.ids.f33.tertiary_text = self.w.forecastDateTime[33].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f33icon.source = 'icons/' + str(self.w.forecastDescIcon[33]) + '.png'

        self.root.ids.f34.text = str(self.w.forecastTemp[34]) + 'F' + ' ' +  self.w.forecastDescription[34].title()
        self.root.ids.f34.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[34]) + ' ' + str(self.w.forecastWindSpeed[34]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[34]) + "%"
        self.root.ids.f34.tertiary_text = self.w.forecastDateTime[34].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f34icon.source = 'icons/' + str(self.w.forecastDescIcon[34]) + '.png'

        self.root.ids.f35.text = str(self.w.forecastTemp[35]) + 'F' + ' ' +  self.w.forecastDescription[35].title()
        self.root.ids.f35.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[35]) + ' ' + str(self.w.forecastWindSpeed[35]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[35]) + "%"
        self.root.ids.f35.tertiary_text = self.w.forecastDateTime[35].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f35icon.source = 'icons/' + str(self.w.forecastDescIcon[35]) + '.png'

        self.root.ids.f36.text = str(self.w.forecastTemp[36]) + 'F' + ' ' +  self.w.forecastDescription[36].title()
        self.root.ids.f36.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[36]) + ' ' + str(self.w.forecastWindSpeed[36]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[36]) + "%"
        self.root.ids.f36.tertiary_text = self.w.forecastDateTime[36].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f36icon.source = 'icons/' + str(self.w.forecastDescIcon[36]) + '.png'

        self.root.ids.f37.text = str(self.w.forecastTemp[37]) + 'F' + ' ' +  self.w.forecastDescription[37].title()
        self.root.ids.f37.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[37]) + ' ' + str(self.w.forecastWindSpeed[37]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[37]) + "%"
        self.root.ids.f37.tertiary_text = self.w.forecastDateTime[37].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f37icon.source = 'icons/' + str(self.w.forecastDescIcon[37]) + '.png'

        self.root.ids.f38.text = str(self.w.forecastTemp[38]) + 'F' + ' ' +  self.w.forecastDescription[38].title()
        self.root.ids.f38.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[38]) + ' ' + str(self.w.forecastWindSpeed[38]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[38]) + "%"
        self.root.ids.f38.tertiary_text = self.w.forecastDateTime[38].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f38icon.source = 'icons/' + str(self.w.forecastDescIcon[38]) + '.png'

        self.root.ids.f39.text = str(self.w.forecastTemp[39]) + 'F' + ' ' +  self.w.forecastDescription[39].title()
        self.root.ids.f39.secondary_text = 'Wd: '  + self.w.windDirection(self.w.forecastWindDeg[39]) + ' ' + str(self.w.forecastWindSpeed[39]) +' MPH' + ' | Hum: ' + str(self.w.forecastHumidity[39]) + "%"
        self.root.ids.f39.tertiary_text = self.w.forecastDateTime[39].strftime('%a: %m/%d/%y %l:%M%p' )
        self.root.ids.f39icon.source = 'icons/' + str(self.w.forecastDescIcon[39]) + '.png'


    def build(self):
        pass



MainApp().run()
