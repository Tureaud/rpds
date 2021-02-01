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
        r = requests.get('https://www.worldometers.info/coronavirus/')
       soup = BeautifulSoup(r.text, 'html.parser')

       test = [0,1,2]
       counter = 0;
       for div in soup.findAll('div',{'class':'maincounter-number'}):
               counter+1
               test.insert(counter, div)

       CVCT = str(test[2])
       CVCT = (re.sub('<[^>]+>','',CVCT)).strip()

       CVCD = str(test[1])
       CVCD = (re.sub('<[^>]+>','',CVCD)).strip()

       CVCR = str(test[0])

       CVCR = (re.sub('<[^>]+>','',CVCR)).strip()

       display.lcd_display_string("WW Covid Cases:",1)
       display.lcd_display_string(CVCT,2)
       print("WW Covid Cases:")
       print(CVCT)
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()

       display.lcd_display_string("WW Deaths:",1)
       display.lcd_display_string(CVCD,2)
       print("WW Deaths:")
       print(CVCD)
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()

       display.lcd_display_string("WW Recoveries:",1)
       display.lcd_display_string(CVCR,2)
       print("WW Recoveries:")
       print(CVCR)
       print("Sleeping 10 seconds")
       print("---------------------")
       time.sleep(10)
       display.lcd_clear()     
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    display.lcd_clear()
