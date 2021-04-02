import wx
import views
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class MainController:
    def __init__(self):
        foFrame = MyFrameFo(None, wx.ID_ANY, "")
        foFrame.Show()
