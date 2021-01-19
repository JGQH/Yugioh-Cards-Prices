from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton, QLineEdit
from PyQt5.Qt import QApplication
from Extras.WebCard import WebCard
from Extras.WebTable import WebTable
from Extras.WebEncryptor import encrypt_code
import json

class MdiSearcher(QMdiSubWindow):
    def __init__(self, parent, deckName:str, cardList:list, dataType:str):
        super().__init__(parent)
        self.setGeometry(0, 0, 16+500, 33+600)
        self.main = parent
        self.cardList = cardList

        self.setFrame(deckName, dataType)
        self.showTotal()

    def setFrame(self, deckName:str, dataType:str):
        self.setWindowTitle(".:. {name} .:.".format(
            name=deckName
        ))

        tblSearches = WebTable(self, self.main, dataType)
        tblSearches.move(8+10, 25+10)
        tblSearches.resize(480, 550)
        tblSearches.addRows(self.cardList)
        self.setWidget(tblSearches)

    def copyCode(self):
        print("Copied code to clipboard")
        code = "|".join([card.getCode() for card in self.cardList])

        clipboard = QApplication.clipboard()
        clipboard.setText(encrypt_code(code))
        pass

    def showTotal(self)->int:
        price = 0
        for card in self.cardList:
            price += card.getPrice()
        return price