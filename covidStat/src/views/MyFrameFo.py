# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Apr  2 13:15:38 2021
#

import wx
from datetime import datetime

# begin wxGlade: dependencies
# end wxGlade
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat
from controllers.main_controller import MainController
from controllers.mondjam_controller import mondjamController
from controllers.mutassam_controller import mutassamController

# begin wxGlade: extracode
# end wxGlade


class MyFrameFo(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameFo.__init__
        kwds["style"] = (
            kwds.get("style", 0)
            | wx.BORDER_SIMPLE
            | wx.CAPTION
            | wx.CLIP_CHILDREN
            | wx.CLOSE_BOX
            | wx.FRAME_NO_TASKBAR
            | wx.FULL_REPAINT_ON_RESIZE
            | wx.ICONIZE
            | wx.MINIMIZE_BOX
            | wx.SYSTEM_MENU
        )
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 391))
        self.SetTitle("Quarantine CountDown")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(
            wx.Bitmap(
                "C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\maskIcon.png",
                wx.BITMAP_TYPE_ANY,
            )
        )
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(110, 149, 195))
        self.SetFont(
            wx.Font(
                9,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                0,
                "MV Boli",
            )
        )
        self.SetToolTip("Going to be better soon...:)")
        self.Hide()

        self.frame_statusbar = self.CreateStatusBar(1)
        self.frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_statusbar_fields = ["frame_statusbar"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.kezdoPanel = wx.Panel(self, wx.ID_ANY)
        self.kezdoPanel.SetBackgroundColour(wx.Colour(110, 149, 195))
        self.kezdoPanel.SetFont(
            wx.Font(
                9,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_1.Add(self.kezdoPanel, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.mondjamBtn = wx.Button(
            self.kezdoPanel, wx.ID_ANY, "Mondjam...", style=wx.BU_AUTODRAW
        )
        self.mondjamBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.mondjamBtn.SetFont(
            wx.Font(
                24,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_2.Add(
            self.mondjamBtn,
            1,
            wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT | wx.TOP,
            47,
        )

        label_1 = wx.StaticText(
            self.kezdoPanel, wx.ID_ANY, "vagy", style=wx.ST_ELLIPSIZE_MIDDLE
        )
        label_1.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_2.Add(
            label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.FIXED_MINSIZE, 30
        )

        self.mutassamBtn = wx.Button(
            self.kezdoPanel, wx.ID_ANY, "Mutassam?", style=wx.BU_AUTODRAW
        )
        self.mutassamBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.mutassamBtn.SetFont(
            wx.Font(
                24,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_2.Add(
            self.mutassamBtn,
            1,
            wx.BOTTOM
            | wx.EXPAND
            | wx.LEFT
            | wx.RESERVE_SPACE_EVEN_IF_HIDDEN
            | wx.RIGHT,
            47,
        )

        self.kezdoPanel.SetSizer(sizer_2)

        self.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade

        MainController(self)
        # mondjamController(self.kezdoPanel)
        # mutassamController(kezdoPanel)
        self.frame_statusbar.SetStatusText("Jóreggelt!")

    def click_frameValto(self, event):  # wxGlade: MyFrameFo.<event_handler>
        print("Event handler 'click_frameValto' not implemented!")
        event.Skip()

    # end of class MyFrameFo

    def idoSzerintKoszon():
        d = datetime.now
