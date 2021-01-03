from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton
from Extras.WebCard import WebCard
from Extras.WebTable import WebTable
import json

class MdiSearcher(QMdiSubWindow):
    isShown = False

    def __init__(self, parent):
        super().__init__(parent)
        MdiSearcher.isShown = True
        self.setGeometry(0, 0, 16+500, 33+600)
        self.main = parent
        self.setFrame()
        self.showTotal()

    def closeEvent(self, event):
        MdiSearcher.isShown = False
        event.accept()

    def setFrame(self):
        self.setWindowTitle(".:. Searcher .:.")

        lblTotal = QLabel(self)
        lblTotal.move(8+10, 25+570)
        lblTotal.resize(480, 20)
        self.lblTotal = lblTotal

        tblSearches = WebTable(self, self.main)
        tblSearches.move(8+10, 25+10)
        tblSearches.resize(480, 550)
        tblSearches.addRows(self.main.cardList)

    def showTotal(self):
        price = 0
        for key in self.main.cardList:
            card:WebCard = self.main.cardList[key]
            price += card.getPrice()
        self.lblTotal.setText("Total price: $%s" % "{:.2f}".format(price))