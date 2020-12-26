from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton
import json

class MdiSearcher(QMdiSubWindow):
    isShown = False

    def __init__(self, parent):
        super().__init__(parent)
        MdiSearcher.isShown = True
        self.setGeometry(0, 0, 16+300, 33+600)
        self.main = parent
        self.setFrame()

    def closeEvent(self, event):
        MdiSearcher.isShown = False
        event.accept()

    def setFrame(self):
        self.setWindowTitle(".:. Searcher .:.")

        #Searcher
        lblSearch = QLabel(self)
        lblSearch.setText("Write the exact name of the card (English):")
        lblSearch.resize(280, 10)
        lblSearch.move(8+10, 25+10)

        lieSearch = QLineEdit(self)
        lieSearch.resize(200, 20)
        lieSearch.move(8+10, 25+30)
        lieSearch.setMaxLength(50)

        btnSearch = QPushButton(self)
        btnSearch.resize(70, 22)
        btnSearch.move(8+220, 25+29)
        btnSearch.setText("Search")

        def doSearch():
            cardName = lieSearch.text()
            btnSearch.setEnabled(False)
            results = self.main.showScraper(cardName)
            
            if(results["status"] == "success"):
                print(json.dumps(results, indent=3))
                lieSearch.clear()
            btnSearch.setEnabled(True)
        btnSearch.clicked.connect(doSearch)
