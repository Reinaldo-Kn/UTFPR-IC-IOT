from FakeSensor import *

UTF_PROVIDER_TOKEN = 'a62102c2893cabed976f59162f6d4125059b31ead23a5fa7ce18d9c6627bf426'

fake_temp_sensor = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'TEMP_SENSOR')
fake_temp_sensor.send_data(24)