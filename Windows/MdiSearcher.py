from PyQt5.QtWidgets import QMdiSubWindow, QLabel, QLineEdit, QPushButton

class MdiSearcher(QMdiSubWindow):
    isShown = False

    def __init__(self, parent):
        super().__init__(parent)
        MdiSearcher.isShown = True
        self.setGeometry(0, 0, 16+300, 33+600)
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

        def doSearch():
            print(lieSearch.text())

        btnSearch = QPushButton(self)
        btnSearch.resize(70, 22)
        btnSearch.move(8+220, 25+29)
        btnSearch.setText("Search")
        btnSearch.clicked.connect(doSearch)