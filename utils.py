import requests
import os
from os.path import join, dirname 
from dotenv import load_dotenv

class weatherApi():
  def __init__(self) -> None:
    try:
      dotenv_path = join(dirname(__file__),'env/.env')
      load_dotenv(dotenv_path)
    except Exception as e:
      print ('Error dotenv...',e)
    
    self.__apiKey = os.environ.get('weatherApiKey')
    self.url='http://api.openweathermap.org/data/2.5/weather'
    self.cityNames=['Grytviken','Faaa']
  
  def currentWeather_byCityName(self,city_name=str) -> dict:
    
    params={
      'q': city_name,
      'appid': self.__apiKey
    }

    r = requests.get(self.url,params=params)
    
    if r.status_code==200:
      return r.json()
    else:
      print('Error request: ',r.status_code)
      return {}

class git():
  def __init__(self) -> None:
    try:
      dotenv_path = join(dirname(__file__),'env/.env')
      load_dotenv(dotenv_path)
    except Exception as e:
      print ('Error dotenv...',e)
    
    self.__apiKey = os.environ.get('githubA piKey')

  def connect(self):
    pass

  def push(self):
    pass

  def createReadme(self):
    pass


if __name__=='__main__':
  print (weatherApi().currentWeather_byCityName(city_name='Timbuktu'))
  pass