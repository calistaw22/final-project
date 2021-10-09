#Import 
import requests 

#Request data
def weather_data(query):
  #API information
  api_key="0132b3854768cc4fe4bfffb6e6a35c85"
  base_url="http://api.openweathermap.org/data/2.5/forecast?id=524901"
  complete_url=base_url+"&"+"appid="+app_key+query
  res=requests.get(complete_url)
  return res.json()
#display results
def display_results(weathers,city):
   print("{}'s temperature: {}°C ".format(city,weathers['main']['temp']))
   print("Wind speed: {} m/s".format(weathers['wind']['speed']))
   print("Description: {}".format(weathers['weather'][0]['description']))
   print("Weather: {}".format(weathers['weather'][0]['main']))
#main function
def main():
  #city information
  city=input("Enter city name: ")
  print()
  #Try block
  try:
    query='q'+city
    w_data=weather_data(query)
    display_results(w_data,city)
    print()
 except:
  print("City is not found")
if __name__=='__main__':
  main()
