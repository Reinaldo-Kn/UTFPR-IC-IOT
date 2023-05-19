from FakeSensor import *
from random import randint
from time import sleep
import json
UTF_PROVIDER_TOKEN = 'ff32e43fcc89a7a5022e37595cddfe69c55454f7d0a0b3a1d83844a458185103'
TEMP_STATION_TOKEN = 'ea372d051b858665dac430feda19fb73c01a420e04ff1acb1bddf301ad357732'

fake_temp_sensor1 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp1')
fake_temp_sensor2 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp2')

big_provider_sensor1 = FakeSensor(TEMP_STATION_TOKEN, 'ESTACAO_DE_TEMPERATURA', 'SENSOR_1')

acc = 0
long = -53.760350
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
    long = long + 0.00001
    fake_temp_sensor1.send_data({
        "observations":[{
            "value": json.dumps({
                "value": rand,
                "component": "COMP1"
            }),
            "location": "-24.7259747 " +str(long)
        }]
    })
    print(rand)
    sleep(5)