from src import weatherApi,git

def createReadMe(location, num_day):
  data = weatherApi().currentWeather_byCityName(city_name=location)
  content = f""" 
  # Did you know that... 
  ## Today the weather in {location} is:

   <div class="row" style = "display:flex">
    <div class="column" style = "flex:50%">
      <table style="margin:5%;margin-top:0px">
        <tr>
          <th>key</th>
          <th>value</th>
        </tr>
        <tr>
          <td>Weather</td>
          <td>{data['weather'][0]['description']}</td>
        </tr>
        <tr>
          <td>Temp feels like</td>
          <td>{round(data['main']['feels_like']-273.15,2)} °C</td>
        </tr>
         <tr>
          <td>Pressure </td>
          <td>{data['main']['pressure']} hPa</td>
        </tr>
         <tr>
          <td>Longitude</td>
          <td>{data['coord']['lon']}</td>
        </tr>
         <tr>
          <td>Latitude</td>
          <td>{data['coord']['lat']}</td>
        </tr>
      </table> 
    </div>
    <div class="column"style = "flex:50%">
      <img src="{location}.png"
        alt="Map {location}"
        style="float: left; margin-right: 10px;" />
    </div>
  </div> 

  ### for more info about this project check [`info.md`](#info.md)
  """
  with open('README.md','w') as f:
    f.write(content)
  

if __name__ == '__main__':
  
  createReadMe('Timbuktu',3)
  #git().pushToGithub(filename='README.md',repo='Im-working-hard',branch='main')