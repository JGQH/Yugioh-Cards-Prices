from PyQt5.QtWidgets import QMdiSubWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MdiAds(QMdiSubWindow):
    isShown = False
    adUrl = u'http://elukia.pythonanywhere.com/advertisement'
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(16+320, 33+180)
        self.setFrame()

    def closeEvent(self, event):
        event.ignore()

    def setFrame(self):
        self.setWindowTitle(".:. Advertisement .:.")

        wevAd = QWebEngineView()
        self.setWidget(wevAd)

        wevAd.load(QUrl(MdiAds.adUrl))
        wevAd.show()