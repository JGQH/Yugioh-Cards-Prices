import json

class WebCard():
    def __init__(self, cardId:int, cardData:dict):
        self.isShown = False

        self.id = hex(cardId)[2::]
        self.name = cardData["name"]
        self.data = cardData["data"]
        self.quantity = cardData["quantity"]

        self.selectedPrice = {
            "index": len(self.data) - 1,
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

    def getCode(self)->str:
        return ".".join([
            self.id,
            str(self.selectedPrice["index"]),
            str(self.selectedPrice["tag"]),
            str(self.quantity)
        ])

    def setTag(self, tag):
        index = self.selectedPrice["index"]
        self.selectedPrice["tag"] = tag
        return self.data[index]["prices"][tag]

    def setIndex(self, index)->str:
        self.selectedPrice["index"] = index
        return self.data[index]["rarity"]