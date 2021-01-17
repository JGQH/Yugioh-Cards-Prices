from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QComboBox, QSpinBox
from Extras.WebCard import WebCard

class MdiViewer(QMdiSubWindow):
    def __init__(self, parent, card:WebCard, setPrice):
        super().__init__(parent)
        self.card = card
        self.main = parent
        self.setGeometry(0, 0, 16+240, 33+130)
        self.setFrame(setPrice)

    def closeEvent(self, event):
        self.card.isShown = False
        event.accept()
    
    def setFrame(self, setPrice):
        self.setWindowTitle(".:. {name} .:.".format(
            name=self.card.name
        ))
        self.card.isShown = True

        #Select card set
        lblSet = QLabel(self)
        lblSet.move(8+10, 25+10)
        lblSet.resize(210, 20)
        lblSet.setText("Select origin:")

        lstSet = QComboBox(self)
        lstSet.move(8+10, 25+40)
        lstSet.resize(210, 20)
        lstSet.addItems(self.card.getSets())

        #Rarity display
        lblRarity = QLabel(self)
        lblRarity.move(8+10, 25+70)
        lblRarity.resize(70, 40)

        #Select Price
        lblPrice = QLabel(self)
        lblPrice.move(8+90, 25+70)
        lblPrice.resize(70, 20)

        lstPrice = QComboBox(self)
        lstPrice.move(8+90, 25+100)
        lstPrice.resize(70, 20)
        lstPrice.addItems(["Lowest", "Average", "Highest"])

        #Select Quantity
        lblQuantity = QLabel(self)
        lblQuantity.move(8+180, 25+70)
        lblQuantity.resize(50, 20)
        lblQuantity.setText("Quantity:")

        spbQuantity = QSpinBox(self)
        spbQuantity.move(8+180, 25+100)
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