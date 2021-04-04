import wx

# import views
from views.MyFrameMondjam import MyFrameMondjam
from views.MyFrameMutassam import MyFrameMutassam
from models import conzolosCovidStat

class MainController:
    def __init__(self, foFrame):
        # self.foFrame = MyFrameFo(None, wx.ID_ANY, "")
        self.foFrame = foFrame
        self.model = conzolosCovidStat.FoCucc()
        #adatlekeres/iras netrol
        self.on_init_foFrame()


        # button handlerek:
        self.foFrame.Bind(wx.EVT_BUTTON, self.click_frameValto, self.foFrame.mondjamBtn)
        self.foFrame.Bind(
            wx.EVT_BUTTON, self.click_frameValto, self.foFrame.mutassamBtn
        )

        # mutassamFrame cuccai
        self.mutassamFrame = MyFrameMutassam(None, wx.ID_ANY, "")
        self.mutassamFrame.Bind(
            wx.EVT_BUTTON, self.click_frameValto, self.mutassamFrame.visszaBtn
        )


        # mondjamframe cuccai
        self.mondjamFrame = MyFrameMondjam(None, wx.ID_ANY, "")
        self.mondjamFrame.Bind(
            wx.EVT_BUTTON, self.click_frameValto, self.mondjamFrame.visszaBtn
        )
        self.mondjamFrame.Bind(
            wx.EVT_BUTTON, self.click_frameValto, self.mondjamFrame.visszaBtn_kozep
        )
        self.mondjamFrame.Bind(
            wx.EVT_BUTTON, self.click_frameValto, self.mondjamFrame.visszaBtn_Jo
        )

        self.foFrame.Show()
    #functionok
    def click_frameValto(self, event):
        buttonDict = {}
        print(event.GetId())
        # print(event.values) mondjamBtnId= -31992 mutassam: 0 vissza: -31974, jo:-31963, közep:-31969
        if event.GetId() == (-31992):
            buttonDict = {self.foFrame: self.mondjamFrame}
        elif event.GetId() == (-31990):
            buttonDict = {self.foFrame: self.mutassamFrame}
        elif event.GetId() == (-31982):
            buttonDict = {self.mutassamFrame: self.foFrame}
        else:
            print(event.GetId())
            buttonDict = {self.mondjamFrame: self.foFrame}

        self.click_valto(buttonDict)
        event.Skip()

    def click_valto(self, buttonDict):
        for key, value in buttonDict.items():
            key.Hide()
            value.Show()

   
    def on_init_foFrame(self):
        self.model.adatIras(self.model.voltEmarMamentes())