from FakeSensor import *
from random import randint
from time import sleep

AIR_QUALITY_PROVIDER_TOKEN = '39f82fde822f86520259871b4ceaf91306da76583f1743a2004ebbdac7ac2d1b'
# Instantiating sensors

# - COMP1 sensors config
token = AIR_QUALITY_PROVIDER_TOKEN
provider_name  = 'AIR_QUALITY_PROVIDER'
location = '-24.73326751241871 -53.76481221537956'

comp1_temp_sensor = FakeSensor(token, provider_name, 'ESP32_1_TEMP_sensor', location)
comp1_pm10_sensor = FakeSensor(token, provider_name, 'ESP32_1_PM10_sensor', location)
comp1_CO2_sensor = FakeSensor(token, provider_name, 'ESP32_1_CO2_sensor', location)

# - COMP2 sensors config, same provider (token and name)
location = '-24.72461397949373 -53.74502484960853'

comp2_temp_sensor = FakeSensor(token, provider_name, 'ESP32_2_TEMP_sensor', location)
comp2_pm10_sensor = FakeSensor(token, provider_name, 'ESP32_2_PM10_sensor', location)
comp2_CO2_sensor = FakeSensor(token, provider_name, 'ESP32_2_CO2_sensor', location)

while (True):
    # CO2 sensor
    comp1_CO2_sensor.send_data(20.1)
    comp2_CO2_sensor.send_data(20.1)
    # temp sensor
    comp1_temp_sensor.send_data(20.1)
    comp2_temp_sensor.send_data(20.1)
    # pm10 sensor
    comp1_pm10_sensor.send_data(20.1)
    comp2_pm10_sensor.send_data(20.1)
    sleep(5)