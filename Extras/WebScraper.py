import requests
import json

class WebScraper():
    API_URL = "http://elukia.pythonanywhere.com"

    def __init__(self):
        pass

    def doPricing(self, ydk)->dict:
        response = requests.post(
           "{}/process_ydk".format(WebScraper.API_URL), data=ydk
        )

        if(response.status_code == 200):
            return response.json()
        return {}
