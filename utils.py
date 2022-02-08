import requests
import os
from os.path import join, dirname 
from dotenv import load_dotenv
import json

class weatherApi():
  def __init__(self) -> None:
    try:
      dotenv_path = join(dirname(__file__),'env/.env')
      load_dotenv(dotenv_path)
    except Exception as e:
      print ('Error dotenv...',e)
    
    self.__apiKey = os.environ.get('weatherApiKey')
    self.url='http://api.openweathermap.org/data/2.5/weather'
    self.cityNames=['Grytviken','Faaa','Timbuktu']
  
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
    
    self.__apiKey = os.environ.get('githubApiKey')
    self.url = 'https://api.github.com'
  
  def __GET(self,url = str, parameters = {}):
    head = {
      'Accept' : 'application/vnd.github.v3+json',
      'Authorization': 'token '+self.__apiKey
    }

    r = requests.get(url,headers=head,params=parameters)
    if r.status_code == 200:
      return r.json()
    else:
      #poner los errores
      print ('error GET method... code:',r.status_code)
      return {}
  
  def __writeResponses(self, fileName=str, **data_response):
    if not os.path.isdir('./responsesJson'):
      os.mkdir('./responsesJson')

    with open(f'responsesJson/{fileName}.json','w') as f:
      json.dump(data_response,f,indent=2)

  def getRepoInfo(self,owner = 'DanielTaiba', repo = 'Im-working-hard'):
    #https://docs.github.com/en/rest/reference/repos#get-a-repository

    endpoint=f'/repos/{owner}/{repo}'
    response = self.__GET(url=self.url+endpoint)
    self.__writeResponses(fileName='infoRepo',**response)

  def getRepoBranches(self,owner = 'DanielTaiba', repo = 'Im-working-hard'):
    #https://docs.github.com/en/rest/reference/repos#get-a-repository
    endpoint=f'/repos/{owner}/{repo}/branches'
    response = self.__GET(url=self.url+endpoint) #response => list
    print(response)

  def getCommitInfo(self,owner = str, repo = str, **kwargs):
    #https://docs.github.com/en/rest/reference/commits
    endpoint=f'/repos/{owner}/{repo}/commits'
    response = self.__GET(url=self.url+endpoint,parameters=kwargs)
    self.__writeResponses(fileName='infoCommits',**response)

  def pushToGithub(self):
    # https://stackoverflow.com/questions/11801983/how-to-create-a-commit-and-push-into-repo-with-github-api-v3
    # doc : https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents


    pass

  def createReadme(self):
    pass


if __name__=='__main__':
  #print (weatherApi().currentWeather_byCityName(city_name='Timbuktu'))
  #git().getCommitInfo(owner='DanielTaiba',repo='Im-working-hard')
  git().getRepoInfo()
  pass