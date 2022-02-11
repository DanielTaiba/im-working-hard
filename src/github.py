import requests
import os
from os.path import join, dirname 
from dotenv import load_dotenv
import json
import base64
from datetime import datetime

class git():
  def __init__(self) -> None:
    try:
      dotenv_path = join(dirname(__file__),'.env')
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

  def pushToGithub(self,filename = str,repo = str, branch = str):
    # https://stackoverflow.com/questions/11801983/how-to-create-a-commit-and-push-into-repo-with-github-api-v3
    # doc : https://docs.github.com/en/rest/reference/repos
    
    ## Get Data
    endpoint = f'/repos/{self.owner}/{repo}/contents/{filename}'
    data = self.__GET(url=self.url+endpoint+'?ref='+branch)

    #prepare file
    base64content=base64.b64encode(open(filename,"rb").read())

    if base64content.decode('utf-8')+"\n" != data['content']:
      message = json.dumps({"message":f"update {datetime.now()}",
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