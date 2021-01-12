import json

class WebCard():
    def __init__(self, cardName, cardData:dict):
        self.name = cardName
        self.isShown = False
        self.data = cardData["data"]
        self.quantity = cardData["quantity"]

        self.selectedPrice = {
            "index": 0,
            "tag": 1
        }

    def getPrice(self)->float:
        index = self.selectedPrice["index"]
        tag = self.selectedPrice["tag"]
        return self.data[index]["prices"][tag] * self.quantity

    def getSets(self)->list:
        return [info["card_set"] for info in self.data]

    def setTag(self, tag):
        index = self.selectedPrice["index"]
        self.selectedPrice["tag"] = tag
        return self.data[index]["prices"][tag]

    def setIndex(self, index)->str:
        self.selectedPrice["index"] = index
        return self.data[index]["rarity"]