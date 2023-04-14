
import requests
import serial
import time
import subprocess


url = "http://localhost:8081/data/utfpr_provider/utfpr_dht11"


ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
headers = {'IDENTITY_KEY': 'da77e7cbdac54f2edd267898b9358b1edd25c6636671268e09b21692d0b1852a'}


while True:
    time.sleep(10)
    
    temp = ser.readline().decode('utf-8').strip().split()[0]
    temp = float(temp) 
    if temp:
        print (temp)
        print ('--------------')
        urlNew = url + "/" + str(temp)
        response = requests.put(urlNew,headers=headers)
        print(response.status_code) 
        print('++++++++++++++')
        
    else: None
    
    
