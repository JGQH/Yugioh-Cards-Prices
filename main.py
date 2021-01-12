from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea
import sys
import json

from Windows.MdiSearcher import MdiSearcher
from Windows.MdiViewer import MdiViewer
from Windows.MdiLoader import MdiLoader
from Windows.MdiAds import MdiAds
from Extras.WebScraper import WebScraper
from Extras.WebCard import WebCard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cardList = {}
        #Add menu options
        mnbMainMenu = self.menuBar()

        #Searcher
        actDeck = QAction("Upload", self)
        actDeck.triggered.connect(self.showLoader)
        mnbMainMenu.addAction(actDeck)

        #MDI
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #Finish Styling
        self.setWindowTitle("YuGiOh - Cards Prices")
        self.showAd()

    def showAd(self):
        ad = MdiAds(self)
        self.mdi.addSubWindow(ad)
        ad.show()

    def showDeck(self, cardList):
        self.cardList = cardList

        searcher = MdiSearcher(self)
        self.mdi.addSubWindow(searcher)
        searcher.show()

    def showLoader(self):
        if(MdiSearcher.isShown or MdiLoader.isShown): return

        loader = MdiLoader(self)
        self.mdi.addSubWindow(loader)
        loader.show()

    def createScraper(self, cardName)->dict:
        scraper = WebScraper(self)
        return scraper.doSearch(cardName)

    def showViewer(self, card:WebCard, setPrice):
        if(not MdiViewer.isShown):
            viewer = MdiViewer(self, card, setPrice)
            self.mdi.addSubWindow(viewer)
            viewer.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scd_mng = MainWindow()
    scd_mng.showMaximized()
    sys.exit(app.exec())