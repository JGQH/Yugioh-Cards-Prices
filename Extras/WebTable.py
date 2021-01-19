from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from Extras.WebCard import WebCard
from Extras.WebData import WebData

class WebTable(QTableWidget):
    def __init__(self, parent, main, dataType):
        super().__init__(0, 3, parent)
        self.parent = parent
        self.dataType = dataType
        self.main = main

        if(dataType == "WebCard"):
            self.setHorizontalHeaderLabels(["Card Name", "Selected Price", "Changer"])
        else:
            self.setHorizontalHeaderLabels(["Card Name", "Details", "Price"])
        
    def addRows(self, cardList:list):
        if(self.dataType == "WebCard"):
            for card in cardList:
                self.addWebCard(card)
        else:
            for card in cardList:
                self.addWebData(card)
            self.parent.showTotal()


    def addWebData(self, card:WebData):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        detailTag = "%s (%s)" % (card.rarity, card.origin)
        self.setItem(row, 1, QTableWidgetItem(detailTag))

        priceTag = "$%s (x%i)" % ("{:.2f}".format(card.getPrice()), card.quantity)
        self.setItem(row, 2, QTableWidgetItem(priceTag))
        pass

    def addWebCard(self, card:WebCard):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        def setPrice():
            priceTag = "$%s (x%i)" % ("{:.2f}".format(card.getPrice()), card.quantity)
            self.setItem(row, 1, QTableWidgetItem(priceTag))
            
            self.parent.showTotal()
            self.parent.showCode()
        setPrice()

        def doModify():
            self.main.showViewer(card, setPrice)

        btnModify = QPushButton(self)
        btnModify.setText("Modify")
        btnModify.clicked.connect(doModify)

        self.setCellWidget(row, 2, btnModify)