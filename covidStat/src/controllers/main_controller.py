import wx

# import views
from views.MyFrameMondjam import MyFrameMondjam

# from views.MyFrameFo import MyFrameFo
from views.MyFrameMutassam import MyFrameMutassam

# majd ide kellene a többi controllert is beszervezni asszem vagy lehet a myframefobe


class MainController:
    def __init__(self, foFrame):
        # self.foFrame = MyFrameFo(None, wx.ID_ANY, "")
        self.foFrame = foFrame

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

        self.foFrame.Show()

    def click_frameValto(self, event):
        buttonDict = {}
        # print(event.values) mondjamBtnId= -31992 mutassam: 0 vissza: -31974
        if event.GetId() == (-31992):
            buttonDict = {self.foFrame: self.mondjamFrame}
        elif event.GetId() == (-31990):
            buttonDict = {self.foFrame: self.mutassamFrame}
        elif event.GetId() == (-31974):
            buttonDict = {self.mondjamFrame: self.foFrame}
        elif event.GetId() == (-31975):
            buttonDict = {self.mondjamFrame: self.foFrame}
        else:
            print(event.GetId())
            buttonDict = {self.mutassamFrame: self.foFrame}

        self.click_valto(buttonDict)

        # if self.foFrame.mondjamBtn:
        #    print(dir(event))
        # print(event.__dict__)
        # self.foFrame.Hide()
        # self.mondjamFrame.Show()

        event.Skip()

    def click_valto(self, buttonDict):

        for key, value in buttonDict.items():
            key.Hide()
            value.Show()


# MainController()
