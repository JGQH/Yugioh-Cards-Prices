from PyQt5.QtWidgets import QFileDialog
from os import path
from Extras.WebScraper import WebScraper
from Extras.WebCard import WebCard

class WebLoader():
    lastRoute = "C:\\ProjectIgnis\\deck"

    def __init__(self):
        self.cardList = {}

    def loadYdk(self)->bool:
        filename = QFileDialog.getOpenFileName(None, "Open YDK file", WebLoader.lastRoute, "YDK files (*.ydk)")[0]
        WebLoader.lastRoute = path.dirname(filename)

        if(not (filename) == ""):
            ydk = open(filename, mode='r', encoding='unicode_escape').read()

            scraper = WebScraper()
            cardList = scraper.doPricing(ydk)
            
            if(len(cardList) > 0):
                for cardName in cardList:
                    cardData = cardList[cardName]
                    self.cardList[cardName] = WebCard(cardName, cardData)
                return True
        return False