import json

class WebCard():
    def __init__(self, cardName, results):
        self.name = cardName
        self.processData(results["data"])

    def processData(self, data):
        self.data = []
        for info in data:
            price_data = info["price_data"]

            if(price_data["status"] == "success"): #If there's available card info
                price_data = price_data["data"]["prices"]

                self.data.append({
                    "setName": info["name"],
                    "printName": info["print_tag"],
                    "rarity": info["rarity"],
                    "prices": {
                        "lowest": price_data["low"],
                        "average": price_data["average"],
                        "highest": price_data["high"]
                    }
                })