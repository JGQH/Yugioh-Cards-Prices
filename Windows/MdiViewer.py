from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QComboBox
from PyQt5.QtGui import QFont
from Extras.WebCard import WebCard

class MdiViewer(QMdiSubWindow):
    isShown = False

    def __init__(self, parent, card:WebCard, setPrice):
        super().__init__(parent)
        MdiViewer.isShown = True
        self.main = parent
        self.setGeometry(0, 0, 16+230, 33+300)
        self.setFrame(card, setPrice)

    def closeEvent(self, event):
        MdiViewer.isShown = False
        event.accept()
    
    def setFrame(self, card:WebCard, setPrice):
        self.setWindowTitle(".:. Viewer .:.")

        lblName = QLabel(self)
        lblName.move(8+10, 25+10)
        lblName.resize(280, 30)
        lblName.setText(card.name)
        lblName.setFont(QFont("Times", 20, QFont.Bold))
        
        #Select card set
        lblSet = QLabel(self)
        lblSet.move(8+10, 25+50)
        lblSet.resize(210, 20)
        lblSet.setText("Select origin:")

        lstSet = QComboBox(self)
        lstSet.move(8+10, 25+70)
        lstSet.resize(210, 20)
        lstSet.addItems(card.getSets())

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

        #Change set
        def changeSet(index):
            rarity = card.setIndex(index)
            lblRarity.setText("Rarity: \n [%s]" % rarity)
        
        index = card.selectedPrice["index"]
        lstSet.setCurrentIndex(index)
        lstSet.currentIndexChanged.connect(changeSet)
        changeSet(index)

        #Change price
        def changePrice(index):
            price = card.setTag(index)
            lblPrice.setText("Price: $%s" % price)

        tag = card.selectedPrice["tag"]
        lstPrice.setCurrentIndex(tag)
        lstPrice.currentIndexChanged.connect(changePrice)
        changePrice(tag)