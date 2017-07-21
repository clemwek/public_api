import requests
import pprint


class Menu(object):
    def __init__(self):
        self.city = 'Nairobi'
        self.country = 'Kenya'

    def run_menu(self):
        print('--------------------------------------------------------')
        print('-------------welcome to these weather app---------------')
        print('--------------------------------------------------------')
        self.city = input("Please enter city name: ")
        self.country = input("Please enter country name: ")

        query_link = 'http://api.openweathermap.org/data/2.5/weather?q='
        query_link += self.city + ','
        query_link += self.country
        query_link += '&APPID=ab787f95e913417895fb6c6aef427ae6'

        response = requests.get(query_link)
        weather_data = response.json()

        print('--------------------------------------------------------')
        print('-------------these are weather app results--------------')
        print('--------------------------------------------------------')

        pprint.pprint(weather_data)

if __name__ == '__main__':
    menu = Menu()
    menu.run_menu()
