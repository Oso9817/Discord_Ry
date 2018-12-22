import urllib.request, json, sys
from urllib.request import urlopen
from keys_api import w_ground

class weatherGet():

	def __init__(self, state, city):
		self.getWeather(state, city)
		self.getHourWeather(state, city)
		self.returnWeather(state ,city)

	
	def requestUrl(self, url):
		#parses any json format url passed onto it, returns readable format
		response = urlopen(url)
		string = response.read().decode('utf-8')
		jData = json.loads(string)
		
		return jData
		
	def getWeather(self, state, city):
		#calls requestUrl to retrieve and return labeled json data to use as variables
		j = self.requestUrl(f'http://api.wunderground.com/api/' + w_ground + '/conditions/q/{state}/{city}.json')
		
		location = j['current_observation']['display_location']['full']
		temperature = j['current_observation']['temp_f']
		weather = j['current_observation']['weather']
		feels = j['current_observation']['feelslike_f']
		last_update = j['current_observation']['observation_time']
		
		return location, temperature, weather, feels, last_update

	def getHourWeather(self, state, city):
		
		#get hourly weather by 24hr time, returned as a list
		j = self.requestUrl(f'http://api.wunderground.com/api/' + w_ground + '/hourly/q/{state}/{city}.json')
		hours_48 = [f['temp']['english'] for f in j['hourly_forecast'] if f["FCTTIME"]['hour'] in ('10', '13', '16', '19', '22')]
		hours_24 = hours_48[:-1]
		
		return hours_24
		
		#prints weather report in simple readable form
	def returnWeather(self, state, city):
		
		forcast = self.getWeather(state, city)
		time = self.getHourWeather(state, city)

		current_temp = f'\nThe weather in {forcast[0]} is {forcast[2]} at {forcast[1]}F degrees but feels like {forcast[3]}F. \n 10AM....{time[0]}F \n 1PM.....{time[1]}F \n 4PM.....{time[2]}F \n 7PM.....{time[3]}F \n 10PM....{time[4]}F \n {forcast[4]}'
		print(current_temp)
		
		return current_temp

#call it with weatherGet('Pennsylvania', 'State College'.replace(' ', '%20'))
weatherGet('Pennsylvania', 'State College'.replace(' ', '%20'))