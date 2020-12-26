from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea
import sys

from Windows.MdiSearcher import MdiSearcher
from Extras.WebScraper import WebScraper
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Add menu options
        mnbMainMenu = self.menuBar()

        actSearcher = QAction("Search", self)
        actSearcher.triggered.connect(self.showSearcher)
        mnbMainMenu.addAction(actSearcher)

        #MDI
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #Finish Styling
        self.setWindowTitle("Organizador de Horario")

    def showSearcher(self):
        if(not MdiSearcher.isShown):
            searcher = MdiSearcher(self)
            self.mdi.addSubWindow(searcher)
            searcher.show()

    def createScraper(self, cardName)->dict:
        scraper = WebScraper(self)
        return scraper.doSearch(cardName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scd_mng = MainWindow()
    scd_mng.showMaximized()
    sys.exit(app.exec())