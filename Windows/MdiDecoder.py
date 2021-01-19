from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton
from Windows.MdiLoader import MdiLoader

class MdiDecoder(QMdiSubWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.main = parent
        self.setGeometry(0, 0, 16+220, 33+100)

        self.setFrame()

    def setFrame(self):
        self.setWindowTitle(".:. Decoder .:.")

        lblCode = QLabel(self)
        lblCode.move(8+10, 25+10)
        lblCode.resize(200, 15)
        lblCode.setText("Insert the deck code:")

        qleCode = QLineEdit(self)
        qleCode.move(8+10, 25+30)
        qleCode.resize(200, 20)
        qleCode.setPlaceholderText("CODE-GOES-HERE")

        btnCode = QPushButton(self)
        btnCode.move(8+60, 25+60)
        btnCode.resize(100, 30)
        btnCode.setText("Search deck")

        def priceCode():
            loader = MdiLoader(self.main)
            self.main.mdi.addSubWindow(loader)
            
            code = qleCode.text()
            loader.startSearching(code)
            loader.show()
            self.close()
        btnCode.clicked.connect(priceCode)