from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea
from PyQt5.QtGui import QIcon
import os
import sys
import json

from Windows.MdiSearcher import MdiSearcher
from Windows.MdiViewer import MdiViewer
from Windows.MdiLoader import MdiLoader
from Windows.MdiAds import MdiAds
from Windows.MdiDecoder import MdiDecoder
from Extras.WebScraper import WebScraper
from Extras.WebCard import WebCard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadIcon()

        #Add menu options
        mnbMainMenu = self.menuBar()

        #Searcher
        actUpload = QAction("Upload", self)
        actUpload.triggered.connect(self.showLoader)
        mnbMainMenu.addAction(actUpload)

        #Decoder
        actDecoder = QAction("Use code", self)
        actDecoder.triggered.connect(self.showDecoder)
        mnbMainMenu.addAction(actDecoder)

        #MDI
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #Finish Styling
        self.setWindowTitle("YuGiOh - Cards Prices")
        self.showAd()

    def loadIcon(self):
        try:
            basePath = sys._MEIPASS
        except:
            basePath = os.path.abspath(".")
        finalPath = os.path.join(basePath, "appIcon.ico")
        
        self.appIcon = QIcon(finalPath)

    def showAd(self):
        ad = MdiAds(self)
        self.mdi.addSubWindow(ad)
        ad.show()

    def showDeck(self, deckName:str, cardList:list, dataType:str):
        searcher = MdiSearcher(self, deckName, cardList, dataType)
        self.mdi.addSubWindow(searcher)
        searcher.show()

    def showLoader(self):
        if(MdiLoader.isShown): return

        loader = MdiLoader(self)
        self.mdi.addSubWindow(loader)
        if(loader.startLoading()):
            loader.show()
    
    def showDecoder(self):
        if(MdiLoader.isShown): return

        decoder = MdiDecoder(self)
        self.mdi.addSubWindow(decoder)
        decoder.show()

    def createScraper(self, cardName)->dict:
        scraper = WebScraper(self)
        return scraper.doSearch(cardName)

    def showViewer(self, card:WebCard, setPrice):
        if(not card.isShown):
            viewer = MdiViewer(self, card, setPrice)
            self.mdi.addSubWindow(viewer)
            viewer.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scd_mng = MainWindow()
    app.setWindowIcon(scd_mng.appIcon)
    scd_mng.showMaximized()
    sys.exit(app.exec())