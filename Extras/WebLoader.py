from PyQt5.QtWidgets import QFileDialog
from os import path



class WebLoader():
    dbRoute = "C:\\Project Ignis\\expansions\\cards.cdb"
    lastRoute = "C:\\"

    def __init__(self):
        self.cardList = {}

    def loadYdk(self)->bool:
        filename = QFileDialog.getOpenFileName(None, "Open YDK file", WebLoader.lastRoute, "YDK files (*.ydk)")[0]
        WebLoader.lastRoute = path.dirname(filename)
        print(WebLoader.lastRoute)
        if(not (filename) == ""):
            ydk = open(filename, 'r').read()
            print(ydk)
            #return True
        return False