import json

class WebCard():
    def __init__(self, cardData:dict):
        self.isShown = False

        self.name = cardData["name"]
        self.data = cardData["data"][::-1]
        self.quantity = cardData["quantity"]

        self.selectedPrice = {
            "index": 0,
            "tag": 1
        }

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{name} x{quantity}".format(
            name=self.name,
            quantity=self.quantity
        )

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