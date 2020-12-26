from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton
from Extras.WebCard import WebCard
from Extras.WebTable import WebTable
import json

class MdiSearcher(QMdiSubWindow):
    isShown = False

    def __init__(self, parent):
        super().__init__(parent)
        MdiSearcher.isShown = True
        self.setGeometry(0, 0, 16+330, 33+600)
        self.main = parent
        self.setFrame()

    def closeEvent(self, event):
        MdiSearcher.isShown = False
        event.accept()

    def setFrame(self):
        self.setWindowTitle(".:. Searcher .:.")

        #Searcher
        lblSearch = QLabel(self)
        lblSearch.setText("Write the exact name of the card (English):")
        lblSearch.resize(310, 10)
        lblSearch.move(8+10, 25+10)

        lieSearch = QLineEdit(self)
        lieSearch.resize(230, 20)
        lieSearch.move(8+10, 25+30)
        lieSearch.setMaxLength(50)

        btnSearch = QPushButton(self)
        btnSearch.resize(70, 22)
        btnSearch.move(8+250, 25+29)
        btnSearch.setText("Search")

        tblSearches = WebTable(self)
        tblSearches.move(8+10, 25+60)
        tblSearches.resize(310, 530)
        tblSearches.addRows(self.main.cardList)

        def doSearch():
            cardName = lieSearch.text()
            btnSearch.setEnabled(False)
            results = self.main.createScraper(cardName)

            if(results["status"] == "success"):
                card = WebCard(cardName, results)
                if self.main.saveCard(card):
                    tblSearches.addRow(card)
                    lieSearch.clear()
            btnSearch.setEnabled(True)
        btnSearch.clicked.connect(doSearch)