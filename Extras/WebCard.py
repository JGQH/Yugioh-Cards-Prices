import json

class WebCard():
    def __init__(self, cardName, results):
        self.name = cardName
        self.processData(results["data"])
        self.quantity = 1

        self.selectedPrice = {
            "index": len(self.data) - 1,
            "tag": 1
        }

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
                    "prices": [
                        price_data["low"],
                        price_data["average"],
                        price_data["high"]
                    ]
                })

    def getPrice(self)->float:
        index = self.selectedPrice["index"]
        tag = self.selectedPrice["tag"]
        return self.data[index]["prices"][tag] * self.quantity

    def getSets(self)->list:
        return [info["setName"] for info in self.data]

    def setTag(self, tag):
        self.selectedPrice["tag"] = tag
        return self.getPrice()

    def setIndex(self, index)->str:
        self.selectedPrice["index"] = index
        return self.data[index]["rarity"]