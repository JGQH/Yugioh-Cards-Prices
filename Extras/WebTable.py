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
        self.insertRow(0)
        self.setItem(0, 0, QTableWidgetItem("Total Price:"))
        if(self.dataType == "WebCard"):
            self.setItem(0, 1, QTableWidgetItem("$0.00"))

            btnCopy = QPushButton(self)
            btnCopy.setText("Copy code")
            btnCopy.clicked.connect(self.parent.copyCode)
            self.setCellWidget(0, 2, btnCopy)
            for card in cardList:
                self.addWebCard(card)
        else:
            self.setSpan(0, 0, 1, 2)
            self.setItem(0, 2, QTableWidgetItem("$0.00"))
            for card in cardList:
                self.addWebData(card)
            self.showTotal()

    def addWebData(self, card:WebData):
        row = self.rowCount() - 1
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        detailTag = "%s (%s)" % (card.rarity, card.origin)
        self.setItem(row, 1, QTableWidgetItem(detailTag))

        priceTag = "$%s (x%i)" % ("{:.2f}".format(card.getPrice()), card.quantity)
        self.setItem(row, 2, QTableWidgetItem(priceTag))
        pass

    def addWebCard(self, card:WebCard):
        row = self.rowCount() - 1
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(card.name))

        def setPrice():
            priceTag = "$%s (x%i)" % ("{:.2f}".format(card.getPrice()), card.quantity)
            self.setItem(row, 1, QTableWidgetItem(priceTag))
            
            self.showTotal()
        setPrice()

        def doModify():
            self.main.showViewer(card, setPrice)

        btnModify = QPushButton(self)
        btnModify.setText("Modify")
        btnModify.clicked.connect(doModify)

        self.setCellWidget(row, 2, btnModify)

    def showTotal(self):
        price = self.parent.showTotal()
        col = 1 if (self.dataType == "WebCard") else 2
        self.item(self.rowCount() - 1, col).setText("$%s" % "{:.2f}".format(price))