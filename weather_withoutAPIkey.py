#Weather information using API without API Key
import requests  #requests module allows to send http request
cityname=input("please enter city :  ")
number=cityname.isdigit() #checking input is integer
#input validation 
if cityname=="" or number == True :
  print("Invalid city name")
else: 
         url="https://wttr.in/{}".format(cityname)
         response = requests.get(url)
         print(response.text)
         """
         #using format and placeholder{}
         The format() method formats the specified value(s) and insert them inside the string's placeholder.
         txt3 = "My name is {}, I'm {}".format("John",36)
         print(txt3)
         outpot: My name is John, I'm 36
         """

        
        
        


