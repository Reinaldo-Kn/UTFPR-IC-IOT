from FakeSensor import *
from random import randint
from time import sleep
import json
UTF_PROVIDER_TOKEN = '845cc49b8d23737be93b63e78ca7eb1f251f0b8256deb2eca3f4a1e8de0cc3e5'
TEMP_STATION_TOKEN = 'ea372d051b858665dac430feda19fb73c01a420e04ff1acb1bddf301ad357732'

fake_temp_sensor1 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp1')
fake_temp_sensor2 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp2')

big_provider_sensor1 = FakeSensor(TEMP_STATION_TOKEN, 'ESTACAO_DE_TEMPERATURA', 'SENSOR_1')

acc = 0
lat = -24.7259747
while(True):
    rand = randint(10,35)
    # fake_temp_sensor1.send_data({
    #     "observations":[{
    #         "value": rand,
    #         "location": "24.7259747 -53.7603501"
    #     }]
    # })
    # fake_temp_sensor2.send_data({
    #     "observations":[{
    #         "value": rand,
    #         "location": "24.7259747 -53.7603501"
    #     }]
    # })
    lat = lat + 0.00001
    big_provider_sensor1.send_data({
        "observations":[{
            "value": json.dumps({
                "value": rand,
                "component": "COMP1"
            }),
            "location": str(lat)+" -53.760350"
        }]
    })
    print(rand)
    sleep(5)