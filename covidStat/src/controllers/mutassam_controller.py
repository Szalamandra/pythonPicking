import wx
from views.MyFrameMutassam import MyFrameMutassam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mutassamController:
    def __init__(self, frame:MyFrameMutassam):
        self.frame = MyFrameMutassam()
        self.model = FoCucc()
        self.modelAdat= NapiAdat()