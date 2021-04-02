import wx
from views.MyFrameMondjam import MyFrameMondjam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mondjamController:
    def __init__(self, frame: MyFrameMondjam):
        self.frame = MyFrameMondjam()
        self.model = FoCucc()
        self.modelAdat = NapiAdat()
