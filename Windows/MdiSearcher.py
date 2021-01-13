from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton
from Extras.WebCard import WebCard
from Extras.WebTable import WebTable
import json

class MdiSearcher(QMdiSubWindow):
    def __init__(self, parent, cardList:list):
        super().__init__(parent)
        self.setGeometry(0, 0, 16+500, 33+600)
        self.main = parent
        self.cardList = cardList

        self.setFrame()
        self.showTotal()

    def setFrame(self):
        self.setWindowTitle(".:. Searcher .:.")

        lblTotal = QLabel(self)
        lblTotal.move(8+10, 25+570)
        lblTotal.resize(480, 20)
        self.lblTotal = lblTotal

        tblSearches = WebTable(self, self.main)
        tblSearches.move(8+10, 25+10)
        tblSearches.resize(480, 550)
        tblSearches.addRows(self.cardList)

    def showTotal(self):
        price = 0
        for card in self.cardList:
            price += card.getPrice()
        self.lblTotal.setText("Total price: $%s" % "{:.2f}".format(price))