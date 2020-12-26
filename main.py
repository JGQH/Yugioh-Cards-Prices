from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Add menu options
        mnbMainMenu = self.menuBar()

        actSearcher = QAction("Search", self)
        actSearcher.triggered.connect(self.showSearcher)
        mnbMainMenu.addAction(actSearcher)

    def showSearcher(self):
        print("Showing searcher")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scd_mng = MainWindow()
    scd_mng.showMaximized()
    sys.exit(app.exec())