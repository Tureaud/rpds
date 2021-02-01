# Import necessary libraries for communication and display use
import lcddriver
import time
import requests
import re
import time
from bs4 import BeautifulSoup
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# Main body of code
try:
    while True:

       api = ('https://api.openweathermap.org/data/2.5/weather?zip=_&appid=_&units=imperial')
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

       # Remember that your sentences can only be 16 characters long!
       print("Writing to display")
       print("---------------------")
       display.lcd_display_string(str(weatherType),1)
       display.lcd_display_string(str(weatherDescrip),2)
       print(weatherType)
       print(weatherDescrip)
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()

       display.lcd_display_string("Temp:"+str(int(round(weatherTemp)))+"*F",1)
       display.lcd_display_string("Real Feel:"+str(int(round(weatherFeel)))+"*F",2)
       print("Temp:"+str(int(round(weatherTemp)))+"*F")
       print("Real Feel:"+str(int(round(weatherFeel)))+"*F")
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()

       display.lcd_display_string("Humidity:"+str(weatherHumidity)+"%",1)
       display.lcd_display_string("Wind speed:"+str(int(round(weatherWind)))+"MPH",2)
       print("Humidity:"+str(weatherHumidity)+"%")
       print("Wind speed:"+str(int(round(weatherWind)))+"MPH")
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()
       
       display.lcd_clear()
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    display.lcd_clear()
