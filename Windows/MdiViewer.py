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
        lblRarity.move(8+10, 25+70)
        lblRarity.resize(50, 50)

        def changeSet(index):
            rarity = card.getRarity(index)
            lblRarity.setText("Rarity: \n [%s]" % rarity)
        lstSet.currentIndexChanged.connect(changeSet)
        lstSet.setCurrentIndex(0)