from dotenv import load_dotenv
import os
import requests
load_dotenv()

ID_KEY = os.getenv("ID_KEY")
URL_API = os.getenv("URL_API")

class FakeSensor:
    def __init__(self, provider_token, provider, sensor):
        self.sensor = sensor
        self.provider_token = provider_token
        self.provider = provider
        self.headers = {
            "IDENTITY_KEY": self.provider_token,
            'Content-Type': 'application/json'
        }

    def send_data(self, data):
        url = f'{URL_API}data/{self.provider}/{self.sensor}'
        r = requests.put(url=url, headers=self.headers, json=data)
        print(r.status_code)