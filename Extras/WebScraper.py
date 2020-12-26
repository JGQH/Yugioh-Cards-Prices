import requests
import json

class WebScraper():
    def __init__(self, parent):
        self.main = parent

    def doSearch(self, cardName)->dict:
        response = requests.get("http://yugiohprices.com/api/get_card_prices/" + cardName)

        if(response.status_code == 200):
            return response.json()
        else:
            return {
                "status": "fail"
            }