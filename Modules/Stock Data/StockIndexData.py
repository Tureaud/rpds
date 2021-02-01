import requests
import time
import re
from bs4 import BeautifulSoup

while True:
    r = requests.get("https://markets.businessinsider.com/index/dow_jones")
    soup = BeautifulSoup(r.text, "html.parser")

    #Dow Jones 30 Current Index Price
    DJCP = str(soup.find(class_="price-section__current-value"))
    DJCP = (re.sub('<[^>]+>','',DJCP)).strip()

    #Dow Jones 30 Points
    DJP = str(soup.find(class_="price-section__absolute-value"))
    DJP = (re.sub('<[^>]+>','',DJP)).strip()

    #Dow Jones 30 Percentage
    DJPP = str(soup.find(class_="price-section__relative-value"))
    DJPP = (re.sub('<[^>]+>','',DJPP)).strip()
    
    #############################################################

    r = requests.get("https://markets.businessinsider.com/index/s&p_500")
    soup = BeautifulSoup(r.text, "html.parser")
    
    #S&P 500 Current Index Price
    SPCP = str(soup.find(class_="price-section__current-value"))
    SPCP = (re.sub('<[^>]+>','',SPCP)).strip()

    #S&P 500 Points
    SPP = str(soup.find(class_="price-section__absolute-value"))
    SPP = (re.sub('<[^>]+>','',SPP)).strip()

    #S&P 500 Percentage
    SPPP = str(soup.find(class_="price-section__relative-value"))
    SPPP = (re.sub('<[^>]+>','',SPPP)).strip()
    
    #############################################################

    r = requests.get("https://markets.businessinsider.com/index/nasdaq_100")
    soup = BeautifulSoup(r.text, "html.parser")
    
    #NASDAQ 100 Current Index Price
    NCP = str(soup.find(class_="price-section__current-value"))
    NCP = (re.sub('<[^>]+>','',NCP)).strip()

    #NASDAQ 100 Points
    NPP = str(soup.find(class_="price-section__absolute-value"))
    NPP = (re.sub('<[^>]+>','',NPP)).strip()

    #NASDAQ 100 Percentage
    NPPP = str(soup.find(class_="price-section__relative-value"))
    NPPP = (re.sub('<[^>]+>','',NPPP)).strip()
    
    #############################################################

    if(DJP.find("-") != 0):
        DJP = "+" + DJP
    if(SPP.find("-") != 0):
        SPP = "+" + SPP
    if(NPP.find("-") != 0):
        NPP = "+" + NPP

    #############################################################

    if(DJPP.find("-") != 0):
        DJPP = "+" + DJPP
    if(SPPP.find("-") != 0):
        SPPP = "+" + SPPP
    if(NPPP.find("-") != 0):
        NPPP = "+" + NPPP
    print("+------------------------------------------------+")
    print("| [DJIA] Dow Jones 30: " + DJCP + ", " + DJP + ", " + DJPP + " |")
    print("| [INX] S&P 500: " + SPCP + ", " + SPP + ", " + SPPP + "         |")
    print("| [NDX] NASDAQ 100: " + NCP + ", " + NPP + ", " + NPPP + "     |")
    print("+------------------------------------------------+")
    time.sleep(5)
