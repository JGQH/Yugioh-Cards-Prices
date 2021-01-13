from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from Extras.WebCard import WebCard

class WebTable(QTableWidget):
    def __init__(self, parent, main):
        super().__init__(0, 3, parent)
        self.parent = parent
        self.main = main
        self.setHorizontalHeaderLabels(["Card Name", "Selected Price", "Changer"])
        
    def addRows(self, cardList:list):
        for card in cardList:
            self.addRow(card)

    def addRow(self, card:WebCard):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        def setPrice():
            priceTag = "$%s (x%i)" % ("{:.2f}".format(card.getPrice()), card.quantity)
            self.setItem(row, 1, QTableWidgetItem(priceTag))
            self.parent.showTotal()
        setPrice()

        def doModify():
            self.main.showViewer(card, setPrice)

        btnModify = QPushButton(self)
        btnModify.setText("Modify")
        btnModify.clicked.connect(doModify)

        self.setCellWidget(row, 2, btnModify)