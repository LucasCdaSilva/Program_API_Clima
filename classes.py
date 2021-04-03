import requests
import json

class Cidade():

    def __init__(self, nome = "", api_key = "9074e0fa3d8a088ea546ebf944404123", temp = 0.0, speed_vento = 0.0, press = 0.0, humi= 0.0, lon = 0.0, lat = 0.0):

        self.token = api_key
        self.nome = nome
        self.temp = temp
        self.speed_vento = speed_vento
        self.press = press
        self.humi = humi
        self.lon = lon
        self.lat = lat

    def setNome(self, nome):
        self.nome = nome
    

    def clima_temp(self):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(self.nome,self.token)
            response = requests.get(url)
            data = response.json()

            self.temp = data['main']['temp']
            self.speed_vento = data['wind']['speed']
            self.press = data['main']['pressure']
            self.humi = data['main']['humidity']
            self.lon = data['coord']['lon']
            self.lat = data['coord']['lat']
        
        except Exception as error:
            print ("Voce nao esta conseguindo obeter acesso aos dados devido o erro: \n {}".format(error))


    
    def temperatura(self):
        return self.temp/10
    
       
    def vento(self):
        return self.speed_vento 
    
       
    def pressao(self):
        return self.press
    
          
    def humidade(self):
        return self.humi
    
     
    def longitude(self):
        return self.lon 
    
     
    def latitude(self):
        return self.lat
    
    
    def getNome(self):
        return self.nome


class Pais():
    def __init__(self,nome):
        self.nome = nome

    def setNome(self, nome):
        self.nome = nome