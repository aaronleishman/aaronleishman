from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
from kivy.clock import Clock
from weather import Weather

class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        with open('gps_apikey.txt', 'r') as f:
            gps_apikey_id = f.read()
        address = parse.quote(address)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey=" + gps_apikey_id +"&searchtext=" + address
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        print('lat',latitude,'lon', longitude)
        app = App.get_running_app()
        app.w = Weather(str(latitude),str(longitude),app.w.api,app.w.units,self.text_field.text )
        app.updateTemp()
        with open('lat.txt', "w") as f:
            f.write(str(latitude))
        with open('lon.txt', "w") as f:
            f.write(str(longitude))
        with open('addr.txt', "w") as f:
            f.write(str(self.text_field.text))

    def error(self, urlrequest, result):
        print("error")
        print(result)

    def failure(self, urlrequest, result):
        print("failure")
        print(result)
