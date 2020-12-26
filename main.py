from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scd_mng = MainWindow()
    scd_mng.showMaximized()
    sys.exit(app.exec())