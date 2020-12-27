from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea
import sys
import json

from Windows.MdiSearcher import MdiSearcher
from Windows.MdiViewer import MdiViewer
from Extras.WebScraper import WebScraper
from Extras.WebCard import WebCard
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cardList = {}
        #Add menu options
        mnbMainMenu = self.menuBar()

        actSearcher = QAction("Search", self)
        actSearcher.triggered.connect(self.showSearcher)
        mnbMainMenu.addAction(actSearcher)

        #MDI
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #Finish Styling
        self.setWindowTitle("YuGiOh - Cards Prices")

    def showSearcher(self):
        if(not MdiSearcher.isShown):
            searcher = MdiSearcher(self)
            self.mdi.addSubWindow(searcher)
            searcher.show()

    def createScraper(self, cardName)->dict:
        scraper = WebScraper(self)
        return scraper.doSearch(cardName)

    def saveCard(self, card:WebCard)->bool:
        if(card.name in self.cardList): return False #Already in the card list

        self.cardList[card.name] = card
        return True

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