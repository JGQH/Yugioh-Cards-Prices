from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot
import traceback, sys

class WebSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(bool)

class WebLoader(QRunnable):
    def __init__(self, function, ydk):
        super(WebLoader, self).__init__()

        self.signals = WebSignals()
        self.function = function
        self.ydk = ydk

    @pyqtSlot()
    def run(self):
        response = False
        try:
            response = self.function(self.ydk)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
            pass
        else:
            self.signals.result.emit(response)
        finally:
            if(response):
                self.signals.finished.emit()