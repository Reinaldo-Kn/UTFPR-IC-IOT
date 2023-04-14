from FakeSensor import *

UTF_PROVIDER_TOKEN = 'f2005d1817efc0be75d35ce32f230e99a0b8c87631b0f23d0a4f11e09504be08'

fake_temp_sensor = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'TEMP_SENSOR')
fake_temp_sensor.send_data(12)