from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QComboBox, QSpinBox
from PyQt5.QtGui import QFont
from Extras.WebCard import WebCard

class MdiViewer(QMdiSubWindow):
    def __init__(self, parent, card:WebCard, setPrice):
        super().__init__(parent)
        self.card = card
        self.main = parent
        self.setGeometry(0, 0, 16+230, 33+140)
        self.setFrame(setPrice)

    def closeEvent(self, event):
        self.card.isShown = False
        event.accept()
    
    def setFrame(self, setPrice):
        self.setWindowTitle(".:. Viewer .:.")
        self.card.isShown = True

        lblName = QLabel(self)
        lblName.move(8+10, 25+10)
        lblName.resize(280, 30)
        lblName.setText(self.card.name)
        lblName.setFont(QFont("Times", 20, QFont.Bold))
        
        #Select card set
        lblSet = QLabel(self)
        lblSet.move(8+10, 25+50)
        lblSet.resize(210, 20)
        lblSet.setText("Select origin:")

        lstSet = QComboBox(self)
        lstSet.move(8+10, 25+70)
        lstSet.resize(210, 20)
        lstSet.addItems(self.card.getSets())

        #Rarity display
        lblRarity = QLabel(self)
        lblRarity.move(8+10, 25+90)
        lblRarity.resize(70, 40)

        #Select Price
        lblPrice = QLabel(self)
        lblPrice.move(8+90, 25+90)
        lblPrice.resize(70, 20)

        lstPrice = QComboBox(self)
        lstPrice.move(8+90, 25+110)
        lstPrice.resize(70, 20)
        lstPrice.addItems(["Lowest", "Average", "Highest"])

        #Select Quantity
        lblQuantity = QLabel(self)
        lblQuantity.move(8+170, 25+90)
        lblQuantity.resize(50, 20)
        lblQuantity.setText("Quantity:")

        spbQuantity = QSpinBox(self)
        spbQuantity.move(8+170, 25+110)
        spbQuantity.resize(50, 20)
        spbQuantity.setMinimum(1)
        spbQuantity.setValue(self.card.quantity)

        #Change tag
        def changeTag(index):
            price = self.card.setTag(index)
            lblPrice.setText("Price: $%s" % price)
            setPrice()

        tag = self.card.selectedPrice["tag"]
        lstPrice.setCurrentIndex(tag)
        lstPrice.currentIndexChanged.connect(changeTag)

        #Change set
        def changeSet(index):
            rarity = self.card.setIndex(index)
            changeTag(lstPrice.currentIndex())
            lblRarity.setText("Rarity: \n [%s]" % rarity)
        
        index = self.card.selectedPrice["index"]
        lstSet.setCurrentIndex(index)
        lstSet.currentIndexChanged.connect(changeSet)
        changeSet(index)

        #Change Quantity
        def changeQuantity():
            self.card.quantity = spbQuantity.value()
            setPrice()
        spbQuantity.valueChanged.connect(changeQuantity)