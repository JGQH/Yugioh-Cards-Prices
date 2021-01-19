import requests
import json

class WebScraper():
    API_URL = "http://elukia.pythonanywhere.com"

    def __init__(self):
        pass

    def priceCode(self, key:str)->dict:
        response = requests.get(
            "{}/process_key".format(WebScraper.API_URL),
            params={"key":key}
        )

        if(response.status_code == 200):
            return response.json()
        return {}

    def priceYDK(self, ydk)->dict:
        response = requests.post(
           "{}/process_ydk".format(WebScraper.API_URL), data=ydk
        )

        if(response.status_code == 200):
            return response.json()
        return {}
