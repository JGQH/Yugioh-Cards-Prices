from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from Extras.WebCard import WebCard

class WebTable(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 3, parent)
        self.setHorizontalHeaderLabels(["Card Name", "Selected Price", "Changer"])
        
    def addRows(self, cardList:dict):
        for name in cardList:
            card = cardList[name]
            self.addRow(card)

    def addRow(self, card:WebCard):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        priceTag = "$%s (x%i)" % (card.getPrice(), card.quantity)
        self.setItem(row, 1, QTableWidgetItem(priceTag))

        def doModify():
            print("Changing card in row %s (Name: %s)" % (row, card.name))

        btnModify = QPushButton(self)
        btnModify.setText("Modify")
        btnModify.clicked.connect(doModify)

        self.setCellWidget(row, 2, btnModify)