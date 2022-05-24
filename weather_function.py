#Weather information using API with function
import requests   #requests module allows to send http request
cityname=input("please enter city :  ")
number=cityname.isdigit() #checking input is string or not
url="https://api.openweathermap.org/data/2.5/weather?q="+cityname+"&units=metric&appid=your_api_key"
#function getting response(json file) from request
def requestapi(city):
      response = requests.get(url)
      #print(response)//<Response [200]>
      myData = response.json()
      weatherDetails(myData)
#function convert json data into python 
def weatherDetails(myData):
           country=myData['sys']['country']
           Weather=myData['weather'][0]['main']
           Description=myData['weather'][0]['description']
           temp1=myData['main']['temp']
           feelLike=myData['main']['feels_like']
           windspeed=myData['wind']['speed']
           Humidity=myData['main']['humidity']
           weather_list=[country,Weather,Description,temp1,feelLike,windspeed,Humidity]
           displayweather(weather_list)
#function display weather details           
def displayweather(my_list):
       print("Country is  " + my_list[0])
       print("Weather is  "+ my_list[1])
       print("weather Description is  "+str( my_list[2]))
       print("Temprecture is  "+ str(my_list[3])+'\N{DEGREE SIGN}'+"C")
       print("Feels Like  " + str(my_list[4]))
       print("Wind  speed is  "+ str(my_list[5]))
       print("Humidity is " + str(my_list[6]))
#input validation 
if cityname=="" or number == True :
  print("Invalid city name")
else: 
  status=requests.get(url).status_code
  # cheking status of request
  if status!=200:
         print("City Not Found")
  else:
         requestapi(cityname)



