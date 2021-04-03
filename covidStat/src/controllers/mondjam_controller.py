import wx
#from views.MyFrameMondjam import MyFrameMondjam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mondjamController:
    def __init__(self, frameMondjam):
        self.frame = frameMondjam
        self.model = FoCucc()
        self.on_init_mondjam()

    def on_init_mondjam(self):
        adatObjLista = self.model.adatOlvasas()
        self.model.ertekeles(adatObjLista)    
