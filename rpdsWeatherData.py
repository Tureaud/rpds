import requests

api = 'http://api.openweathermap.org/data/2.5/weather?zip=57042&appid=20b04fba04e7d29502d449234e627f47&units=imperial'
data = requests.get(api).json()
#Stores weather id/type
weatherType = data['weather'][0]['main']
#Stores weather id/type description
weatherDescrip = data['weather'][0]['description']
#Stores weather temp
weatherTemp = data['main']['temp']
#Stores "Real feel" temp
weatherFeel = data['main']['feels_like']
#Stores humidity
weatherHumidity = data['main']['humidity']
#Stores windspeed
weatherWind = data['wind']['speed']
#, end='' specifies same line print
print(weatherType,",", weatherDescrip)
print("Current temp:",weatherTemp,"°F")
print("Feels like:",weatherFeel,"°F")
print("Humidity:",weatherHumidity,"%")
print("Wind speed:",weatherWind,"MPH")
