from FakeSensor import *
from random import randint
from time import sleep

UTF_PROVIDER_TOKEN = 'a7e1972c9ccc71d5c27013a3c60fbe335b1038859f5804630f7e2f3152861370'

fake_temp_sensor = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'TEMP_SENSOR')
while(True):
    rand = randint(10,35)
    fake_temp_sensor.send_data(rand)
    print(rand)
    sleep(30)