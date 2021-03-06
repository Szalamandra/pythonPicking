# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Apr  2 13:15:38 2021
#

import wx
# begin wxGlade: dependencies
import wx.grid

# end wxGlade
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat
from controllers.mutassam_controller import mutassamController
from os import path,curdir
covidStatFolder = path.abspath(curdir)       #from os

kepIkonPath = path.join(covidStatFolder, "images//maskIcon.png")
# begin wxGlade: extracode
# end wxGlade


class MyFrameMutassam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameMutassam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((647, 469))
        self.SetTitle("Quarantine CountDown")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(kepIkonPath, wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(110, 149, 195))

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, u"Elmúlt öt nap adatai")
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_2.Add(label_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.LEFT | wx.RIGHT | wx.TOP, 24)

        self.grid_tabla = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.grid_tabla.CreateGrid(5, 2)
        self.grid_tabla.SetRowLabelSize(25)
        self.grid_tabla.SetColLabelSize(26)
        self.grid_tabla.EnableEditing(0)
        self.grid_tabla.EnableDragColSize(0)
        self.grid_tabla.EnableDragRowSize(0)
        self.grid_tabla.EnableDragGridSize(0)
        self.grid_tabla.SetLabelBackgroundColour(wx.Colour(193, 233, 225))
        self.grid_tabla.SetColLabelValue(0, u"Napi Új Fertőzöttek Száma")
        self.grid_tabla.SetColSize(0, 271)
        self.grid_tabla.SetColLabelValue(1, u"Napi Halottak Száma")
        self.grid_tabla.SetColSize(1, 270)
        self.grid_tabla.SetRowSize(0, 30)
        self.grid_tabla.SetRowSize(1, 30)
        self.grid_tabla.SetRowSize(2, 30)
        self.grid_tabla.SetRowSize(3, 30)
        self.grid_tabla.SetRowSize(4, 30)
        self.grid_tabla.SetMinSize((566, 176))
        self.grid_tabla.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, 0, "Malgun Gothic Semilight"))
        sizer_2.Add(self.grid_tabla, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT, 28)

        sizer_2.Add((20, 2), 1, wx.EXPAND, 0)

        self.visszaBtn = wx.Button(self, wx.ID_ANY, u"Szép...", style=wx.BU_AUTODRAW)
        self.visszaBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_2.Add(self.visszaBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.SHAPED, 20)

        self.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade
        mutassamController(self)
        #kozepen legyen a kiiras 
        self.grid_tabla.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        self.grid_tabla.HideCellEditControl()
# end of class MyFrameMutassam
