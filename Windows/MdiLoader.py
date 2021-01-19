from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThreadPool
from Extras.WebScraper import WebScraper
from Extras.WebCard import WebCard
from os import path
from Extras.WebLoader import WebLoader
from Extras.WebData import WebData

class MdiLoader(QMdiSubWindow):
    isShown = False
    lastRoute = "C:\\ProjectIgnis\\deck"

    def __init__(self, parent):
        super().__init__(parent)
        self.main = parent
        self.cardList = []

        self.setGeometry(0, 0, 16+140, 33+55)
    
    def closeEvent(self, event):
        MdiLoader.isShown = False
        event.accept()

    def setFrame(self):
        self.setWindowTitle(".:. {name} .:.".format(
            name=self.name
        ))
        
        lblMsg = QLabel(self)
        lblMsg.move(8+10, 25+10)
        lblMsg.resize(120, 35)
        lblMsg.setFont(QFont("Times", 20, QFont.Bold))
        lblMsg.setText("Loading...")
    
    #======================================================#
    #==================== CODE-RELATED ====================#
    #======================================================#
    def startSearching(self, code:str):
        MdiLoader.isShown = True
        self.name = "[CODE].ydk"
        self.setFrame()
            
        loader = WebLoader(self.priceCode, code)
        loader.signals.finished.connect(self.revealCode)
        loader.signals.result.connect(self.print_output)
        loader.signals.error.connect(self.print_error)
        QThreadPool(self).start(loader)

    def priceCode(self, code:str)->bool:
        scraper = WebScraper()
        cardList = scraper.priceCode(code)

        if(len(cardList) > 0):
            for cardId in cardList:
                card = WebData(cardList[cardId])

                self.cardList.append(card)
            return True
        return False

    #=====================================================#
    #==================== YDK-RELATED ====================#
    #=====================================================#
    def startLoading(self)->bool:
        if(ydk := self.loadYDK()):
            MdiLoader.isShown = True
            self.setFrame()
            
            loader = WebLoader(self.priceYDK, ydk)
            loader.signals.finished.connect(self.revealYDK)
            loader.signals.result.connect(self.print_output)
            loader.signals.error.connect(self.print_error)
            QThreadPool(self).start(loader)

            return True
        return False

    def loadYDK(self):
        filename = QFileDialog.getOpenFileName(None, "Open YDK file", MdiLoader.lastRoute, "YDK files (*.ydk)")[0]
        MdiLoader.lastRoute = path.dirname(filename)

        if(filename == ""): return None

        self.name = path.basename(filename)

        ydk = open(filename, mode='r', encoding='unicode_escape').read()
        return ydk

    def priceYDK(self, ydk)->bool:
        scraper = WebScraper()
        cardList = scraper.priceYDK(ydk)

        if(len(cardList) > 0):
            for cardId in cardList:
                card = WebCard(int(cardId), cardList[cardId])
                self.cardList.append(card)
            return True
        return False

    #========================================================#
    #==================== THREAD-RELATED ====================#
    #========================================================#
    def revealCode(self):
        print(self.cardList)
        self.main.showDeck(self.name, self.cardList, "WebData")
        self.close()

    def revealYDK(self):
        print(self.cardList)
        self.main.showDeck(self.name, self.cardList, "WebCard")
        self.close()

    def print_output(self, result):
        print("OUTPUT:")
        print(result)

    def print_error(self, error):
        print("ERROR:")
        print(error)
        self.close()