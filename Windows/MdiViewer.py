from PyQt5.QtWidgets import QMdiSubWindow, QLabel
from PyQt5.QtGui import QFont
from Extras.WebCard import WebCard

class MdiViewer(QMdiSubWindow):
    isShown = False

    def __init__(self, parent, card:WebCard, setPrice):
        super().__init__(parent)
        MdiViewer.isShown = True
        self.main = parent
        self.setGeometry(0, 0, 16+300, 33+300)
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