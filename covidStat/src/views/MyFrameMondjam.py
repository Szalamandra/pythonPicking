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
from controllers.mondjam_controller import mondjamController

# begin wxGlade: extracode
# end wxGlade


class MyFrameMondjam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameMondjam.__init__
        kwds["style"] = (
            kwds.get("style", 0)
            | wx.CAPTION
            | wx.CLIP_CHILDREN
            | wx.CLOSE_BOX
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
        self.Hide()

        sizer_myFrameMondjam = wx.BoxSizer(wx.HORIZONTAL)

        self.panelFo_ertekelesRossz = wx.Panel(self, wx.ID_ANY)
        sizer_myFrameMondjam.Add(self.panelFo_ertekelesRossz, 1, wx.EXPAND, 0)

        sizer_ertekelesFo = wx.BoxSizer(wx.VERTICAL)

        self.panel_ertekeles_rossz = wx.Panel(self.panelFo_ertekelesRossz, wx.ID_ANY)
        sizer_ertekelesFo.Add(self.panel_ertekeles_rossz, 1, wx.EXPAND, 0)

        sizer_ertekeles_rossz_kep = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_1 = wx.StaticBitmap(
            self.panel_ertekeles_rossz,
            wx.ID_ANY,
            wx.Bitmap(
                "C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/projektek/covidStat/images/walkSmall.gif",
                wx.BITMAP_TYPE_ANY,
            ),
        )
        sizer_ertekeles_rossz_kep.Add(
            bitmap_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10
        )

        self.panel_ertekeles_rossz_szoveg = wx.Panel(
            self.panelFo_ertekelesRossz, wx.ID_ANY
        )
        sizer_ertekelesFo.Add(self.panel_ertekeles_rossz_szoveg, 1, wx.EXPAND, 0)

        sizer_ertekeles_kozep_kep = wx.BoxSizer(wx.HORIZONTAL)

        label_1 = wx.StaticText(
            self.panel_ertekeles_rossz_szoveg,
            wx.ID_ANY,
            u"Sajnos még messze van az ünneplés...",
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        label_1.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                0,
                "Segoe Print",
            )
        )
        label_1.Wrap(300)
        sizer_ertekeles_kozep_kep.Add(
            label_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 9
        )

        self.panel_panel_ertekeles_rosszBtn = wx.Panel(
            self.panelFo_ertekelesRossz, wx.ID_ANY
        )
        sizer_ertekelesFo.Add(self.panel_panel_ertekeles_rosszBtn, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)

        self.visszaBtn = wx.Button(
            self.panel_panel_ertekeles_rosszBtn,
            wx.ID_ANY,
            u"Nincs mit tenni, megértettem...",
            style=wx.BU_AUTODRAW,
        )
        self.visszaBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_6.Add(self.visszaBtn, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panelFo_ertekelesKozep = wx.Panel(self, wx.ID_ANY)
        sizer_myFrameMondjam.Add(self.panelFo_ertekelesKozep, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        self.panel_ertekeles_KozepKep = wx.Panel(self.panelFo_ertekelesKozep, wx.ID_ANY)
        sizer_5.Add(self.panel_ertekeles_KozepKep, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_2 = wx.StaticBitmap(
            self.panel_ertekeles_KozepKep,
            wx.ID_ANY,
            wx.Bitmap(
                "C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\prepareSmall.gif",
                wx.BITMAP_TYPE_ANY,
            ),
        )
        sizer_8.Add(
            bitmap_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10
        )

        self.panel_ertekeles_kozep_szoveg = wx.Panel(
            self.panelFo_ertekelesKozep, wx.ID_ANY
        )
        sizer_5.Add(self.panel_ertekeles_kozep_szoveg, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)

        label_2 = wx.StaticText(
            self.panel_ertekeles_kozep_szoveg,
            wx.ID_ANY,
            u"Készülj az ünneplésre...",
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        label_2.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                0,
                "Segoe Print",
            )
        )
        label_2.Wrap(300)
        sizer_9.Add(
            label_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10
        )

        self.panel_ertekeles_kozepBtn = wx.Panel(self.panelFo_ertekelesKozep, wx.ID_ANY)
        sizer_5.Add(self.panel_ertekeles_kozepBtn, 1, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_10.Add(sizer_2, 0, 0, 0)

        label_4 = wx.StaticText(
            self.panel_ertekeles_kozepBtn, wx.ID_ANY, u"Elmúlt 5 nap adatai"
        )
        label_4.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_2.Add(label_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 9)

        self.grid_tabla = wx.grid.Grid(
            self.panel_ertekeles_kozepBtn, wx.ID_ANY, size=(1, 1)
        )
        self.grid_tabla.CreateGrid(5, 2)
        self.grid_tabla.SetRowLabelSize(29)
        self.grid_tabla.SetColLabelSize(36)
        self.grid_tabla.EnableEditing(0)
        self.grid_tabla.SetGridLineColour(wx.Colour(255, 255, 255))
        self.grid_tabla.SetLabelBackgroundColour(wx.Colour(219, 240, 240))
        self.grid_tabla.SetColLabelValue(0, u"Napi Uj Fertőzöttek száma")
        self.grid_tabla.SetColSize(0, 271)
        self.grid_tabla.SetColLabelValue(1, u"Napi Halotta Száma")
        self.grid_tabla.SetColSize(1, 271)
        self.grid_tabla.SetRowSize(0, 30)
        self.grid_tabla.SetRowSize(1, 30)
        self.grid_tabla.SetRowSize(2, 30)
        self.grid_tabla.SetRowSize(3, 30)
        self.grid_tabla.SetRowSize(4, 30)
        self.grid_tabla.SetBackgroundColour(wx.Colour(231, 199, 163))
        self.grid_tabla.SetFont(
            wx.Font(
                11,
                wx.FONTFAMILY_MODERN,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "NSimSun",
            )
        )
        sizer_2.Add(
            self.grid_tabla,
            0,
            wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND | wx.SHAPED,
            30,
        )

        sizer_2.Add((20, 24), 1, wx.ALL | wx.EXPAND, 0)

        self.visszaBtn_copy = wx.Button(
            self.panel_ertekeles_kozepBtn, wx.ID_ANY, u"Szép...", style=wx.BU_AUTODRAW
        )
        self.visszaBtn_copy.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn_copy.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_2.Add(
            self.visszaBtn_copy,
            0,
            wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            10,
        )

        self.visszaBtn_kozep = wx.Button(
            self.panel_ertekeles_kozepBtn,
            wx.ID_ANY,
            "Rohanok is a boltba...",
            style=wx.BU_AUTODRAW,
        )
        self.visszaBtn_kozep.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn_kozep.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_10.Add(self.visszaBtn_kozep, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panelFo_ertekelesJo = wx.Panel(self, wx.ID_ANY)
        sizer_myFrameMondjam.Add(self.panelFo_ertekelesJo, 1, wx.EXPAND, 0)

        sizer_11 = wx.BoxSizer(wx.VERTICAL)

        self.panel_ertekeles_joKep = wx.Panel(self.panelFo_ertekelesJo, wx.ID_ANY)
        sizer_11.Add(self.panel_ertekeles_joKep, 1, wx.EXPAND, 0)

        sizer_ertekeles_joKep = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_3 = wx.StaticBitmap(
            self.panel_ertekeles_joKep,
            wx.ID_ANY,
            wx.Bitmap(
                "C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/projektek/covidStat/images/walkSmall.gif",
                wx.BITMAP_TYPE_ANY,
            ),
        )
        sizer_ertekeles_joKep.Add(
            bitmap_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10
        )

        self.panel_ertekeles_joSzoveg = wx.Panel(self.panelFo_ertekelesJo, wx.ID_ANY)
        sizer_11.Add(self.panel_ertekeles_joSzoveg, 1, wx.EXPAND, 0)

        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)

        label_3 = wx.StaticText(
            self.panel_ertekeles_joSzoveg,
            wx.ID_ANY,
            u"Eljött Dionüsszosz Diadalnapja!",
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        label_3.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                0,
                "Segoe Print",
            )
        )
        label_3.Wrap(300)
        sizer_13.Add(
            label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10
        )

        self.panel_ertekeles_joBtn = wx.Panel(self.panelFo_ertekelesJo, wx.ID_ANY)
        sizer_11.Add(self.panel_ertekeles_joBtn, 1, wx.EXPAND, 0)

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)

        self.visszaBtn_Jo = wx.Button(
            self.panel_ertekeles_joBtn,
            wx.ID_ANY,
            "Rohanok is a boltba...",
            style=wx.BU_AUTODRAW,
        )
        self.visszaBtn_Jo.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn_Jo.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "MV Boli",
            )
        )
        sizer_14.Add(self.visszaBtn_Jo, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panel_ertekeles_joBtn.SetSizer(sizer_14)

        self.panel_ertekeles_joSzoveg.SetSizer(sizer_13)

        self.panel_ertekeles_joKep.SetSizer(sizer_ertekeles_joKep)

        self.panelFo_ertekelesJo.SetSizer(sizer_11)

        self.panel_ertekeles_kozepBtn.SetSizer(sizer_10)

        self.panel_ertekeles_kozep_szoveg.SetSizer(sizer_9)

        self.panel_ertekeles_KozepKep.SetSizer(sizer_8)

        self.panelFo_ertekelesKozep.SetSizer(sizer_5)

        self.panel_panel_ertekeles_rosszBtn.SetSizer(sizer_6)

        self.panel_ertekeles_rossz_szoveg.SetSizer(sizer_ertekeles_kozep_kep)

        self.panel_ertekeles_rossz.SetSizer(sizer_ertekeles_rossz_kep)

        self.panelFo_ertekelesRossz.SetSizer(sizer_ertekelesFo)

        self.SetSizer(sizer_myFrameMondjam)

        self.Layout()

        #self.Bind(wx.EVT_BUTTON, self.click_frameValto, self.visszaBtn_copy)
        # end wxGlade


        mondjamController(self)


# end of class MyFrameMondjam
