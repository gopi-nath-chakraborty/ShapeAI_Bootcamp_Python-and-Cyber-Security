# import modules
import requests
from datetime import datetime

# api key
api_key = '6fa75eefa45a217d3aa81006d28ffff7'

# location - weather report of which city
city_name = input('Enter the city name : ')

complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
    city_name+'&appid='+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store data
curr_temp = ((api_data['main']['temp']) - 273.15)
max_temp = ((api_data['main']['temp_max']) - 273.15)
min_temp = ((api_data['main']['temp_min']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
feels_like = ((api_data['main']['feels_like']) - 273.15)
wind_speed = api_data['wind']['speed']
country = api_data['sys']['country']
curr_date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')

# display all the data
print('-------------------------------------------------------------')

print('Weather Stats for - {} || {}'.format(city_name.upper(), curr_date_time))

print('-------------------------------------------------------------')

print('Current Temp : {:.2f} deg C'.format(curr_temp))
print('Max Temp: {:.2f} deg C'.format(max_temp))
print('Min Temp : {:.2f} deg C'.format(min_temp))
print('Weather Description : ', weather_desc.upper())
print('Humidity : ', humidity, '%')
print('Feels Like : {:.2f} deg C'.format(feels_like))
print('Wind Speed : ', wind_speed, 'km/h')
print('Country : ', country)
