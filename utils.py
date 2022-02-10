import requests
import os
from os.path import join, dirname 
from dotenv import load_dotenv
import json
import base64

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
    
    self.url = 'https://api.github.com'
    self.owner ='DanielTaiba'
    self.__headers = {
      'Accept' : 'application/vnd.github.v3+json',
      'Authorization': 'token '+os.environ.get('githubApiKey'),
      "Content-Type": "application/json",
    }
  
  def __GET(self,url = str, parameters = {}):
    r = requests.get(url,headers=self.__headers,params=parameters)
    if r.status_code == 200:
      return r.json()
    else:
      #poner los errores
      print ('error GET method... code:',r.status_code)
      return {}
  
  def __PUT(self,url=str,data={}):
    r = requests.put(url,headers=self.__headers,data=data)
    return r.status_code
  
  
  def __writeResponses(self, fileName=str, **data_response):
    if not os.path.isdir('./responsesJson'):
      os.mkdir('./responsesJson')

    with open(f'responsesJson/{fileName}.json','w') as f:
      json.dump(data_response,f,indent=2)

  def getRepoInfo(self, repo = 'Im-working-hard'):
    #https://docs.github.com/en/rest/reference/repos#get-a-repository

    endpoint=f'/repos/{self.owner}/{repo}'
    response = self.__GET(url=self.url+endpoint)
    self.__writeResponses(fileName='infoRepo',**response)

  def getRepoBranches(self, repo = 'Im-working-hard'):
    #https://docs.github.com/en/rest/reference/repos#get-a-repository
    endpoint=f'/repos/{self.owner}/{repo}/branches'
    response = self.__GET(url=self.url+endpoint) #response => list
    print(response)

  def getCommitInfo(self,repo = str, **kwargs):
    #https://docs.github.com/en/rest/reference/commits
    endpoint=f'/repos/{self.owner}/{repo}/commits'
    response = self.__GET(url=self.url+endpoint,parameters=kwargs)
    self.__writeResponses(fileName='infoCommits',**response)

  def pushToGithub(self,filename,repo, branch):
    # https://stackoverflow.com/questions/11801983/how-to-create-a-commit-and-push-into-repo-with-github-api-v3
    # doc : https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    
    ## Get Data
    endpoint = f'/repos/{self.owner}/{repo}/contents/{filename}'
    data = self.__GET(url=self.url+endpoint+'?ref='+branch)

    #prepare file
    base64content=base64.b64encode(open(filename,"rb").read())

    if base64content.decode('utf-8')+"\n" != data['content']:
      message = json.dumps({"message":"update 2",
                          "branch": branch,
                          "content": base64content.decode("utf-8") ,
                          "sha": data['sha']
                          })

      #put commit
      status = self.__PUT(url=self.url+endpoint,data=message)
      if status == 200:
        print('ok')
      else:
        ## add direct message to email 
        print('error put...',status)

    else:
      print("File no update")


  def createReadme(self):
    pass


if __name__=='__main__':
  #print (weatherApi().currentWeather_byCityName(city_name='Timbuktu'))
  #git().getCommitInfo(owner='DanielTaiba',repo='Im-working-hard')
  git().pushToGithub('README.md','Im-working-hard','main')
  pass