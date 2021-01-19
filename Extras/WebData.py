class WebData():
    def __init__(self, cardData:dict):
        self.name = cardData["name"]
        self.quantity = int(cardData["quantity"])
        self.origin = cardData["card_set"]
        self.rarity = cardData["rarity"]
        self.price = float(cardData["price"])

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{name} x{quantity}".format(
            name=self.name,
            quantity=self.quantity
        )

    def getPrice(self):
        return self.price * self.quantity