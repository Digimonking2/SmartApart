from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# TODO: Change from scimming google result to OpenWeatherMap API

url = "https://www.google.com/search?q=weather%20"+os.environ["city"]

def getWeatherData():
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    # list having all div tags having particular clas sname
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    # particular list with required data
    strd = listdiv[5].text
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]
    return {temp,time,sky,other_data}
