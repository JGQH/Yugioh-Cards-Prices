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

        lblTotal = QLabel(self)
        lblTotal.move(8+10, 25+570)
        lblTotal.resize(140, 20)
        self.lblTotal = lblTotal

        lblCode = QLabel(self)
        lblCode.move(8+160, 25+570)
        lblCode.resize(70, 20)
        lblCode.setText("Deck code:")

        qleCode = QLineEdit(self)
        qleCode.move(8+240, 25+570)
        qleCode.resize(200, 20)
        qleCode.setReadOnly(True)
        self.qleCode = qleCode

        btnCopy = QPushButton(self)
        btnCopy.move(8+450, 25+570)
        btnCopy.resize(40, 20)
        btnCopy.setText("Copy")
        def copy(self):
            print("Copied code to clipboard")
            clipboard = QApplication.clipboard()
            clipboard.setText(qleCode.text())
        btnCopy.clicked.connect(copy)

        tblSearches = WebTable(self, self.main, dataType)
        tblSearches.move(8+10, 25+10)
        tblSearches.resize(480, 550)
        tblSearches.addRows(self.cardList)

    def showCode(self):
        code = "|".join([card.getCode() for card in self.cardList])
        self.qleCode.setText(encrypt_code(code))

    def showTotal(self):
        price = 0
        for card in self.cardList:
            price += card.getPrice()
        self.lblTotal.setText("Total price: $%s" % "{:.2f}".format(price))