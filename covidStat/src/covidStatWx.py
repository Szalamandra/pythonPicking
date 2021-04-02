#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Mar 31 21:38:06 2021
#

import wx

# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrameFo(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameFo.__init__
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.FRAME_NO_TASKBAR | wx.FULL_REPAINT_ON_RESIZE | wx.ICONIZE | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 391))
        self.SetTitle("Quarantine CountDown")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\maskIcon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(110, 149, 195))
        self.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "MV Boli"))
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
        self.kezdoPanel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_1.Add(self.kezdoPanel, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.mondjamBtn = wx.Button(self.kezdoPanel, wx.ID_ANY, "Mondjam...", style=wx.BU_AUTODRAW)
        self.mondjamBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.mondjamBtn.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_2.Add(self.mondjamBtn, 1, wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT | wx.TOP, 47)

        label_1 = wx.StaticText(self.kezdoPanel, wx.ID_ANY, "vagy", style=wx.ST_ELLIPSIZE_MIDDLE)
        label_1.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.FIXED_MINSIZE, 30)

        self.mutassamBtn = wx.Button(self.kezdoPanel, wx.ID_ANY, "Mutassam?", style=wx.BU_AUTODRAW)
        self.mutassamBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.mutassamBtn.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_2.Add(self.mutassamBtn, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 47)

        self.kezdoPanel.SetSizer(sizer_2)

        self.SetSizer(sizer_1)

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.click_frameValto, self.mondjamBtn)
        self.Bind(wx.EVT_BUTTON, self.click_frameValto, self.mutassamBtn)
        # end wxGlade

    def click_frameValto(self, event):  # wxGlade: MyFrameFo.<event_handler>
        #vagyis a self az nem is a button
        #target=dir(self)
        #target=getattribute(self.mutassamBtn)
        #btnFrameDict = {self.mutassamBtn: MyFrameMutassam, self.mondjamBtn: MyFrameMondjam, MyFrameMondjam.visszaBtn: MyFrameFo}
        btnList=[]
        if self.isinstance(MyFrameFo):
            btnList = [self.mutassamBtn, self.mondjamBtn]
        print(dir(MyFrameMondjam))
        print(str(btnList))
        event.Skip() 

# end of class MyFrameFo

class MyFrameMondjam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameMondjam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 391))
        self.SetTitle("Quarantine CountDown")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\maskIcon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(110, 149, 195))
        self.Hide()

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_1 = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/projektek/covidStat/images/walkSmall.gif", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(bitmap_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_3, 1, wx.EXPAND, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)

        label_1 = wx.StaticText(self.panel_3, wx.ID_ANY, u"Sajnos még messze van az ünneplés...", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Segoe Print"))
        label_1.Wrap(300)
        sizer_7.Add(label_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 9)

        self.panel_4 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_4, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)

        self.visszaBtn = wx.Button(self.panel_4, wx.ID_ANY, u"Nincs mit tenni, megértettem...", style=wx.BU_AUTODRAW)
        self.visszaBtn.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_6.Add(self.visszaBtn, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panel_5 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_5, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        self.panel_6 = wx.Panel(self.panel_5, wx.ID_ANY)
        sizer_5.Add(self.panel_6, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_2 = wx.StaticBitmap(self.panel_6, wx.ID_ANY, wx.Bitmap("C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\prepareSmall.gif", wx.BITMAP_TYPE_ANY))
        sizer_8.Add(bitmap_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.panel_7 = wx.Panel(self.panel_5, wx.ID_ANY)
        sizer_5.Add(self.panel_7, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)

        label_2 = wx.StaticText(self.panel_7, wx.ID_ANY, u"Készülj az ünneplésre...", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_2.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Segoe Print"))
        label_2.Wrap(300)
        sizer_9.Add(label_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10)

        self.panel_8 = wx.Panel(self.panel_5, wx.ID_ANY)
        sizer_5.Add(self.panel_8, 1, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)

        self.visszaBtn_copy = wx.Button(self.panel_8, wx.ID_ANY, "Rohanok is a boltba...", style=wx.BU_AUTODRAW)
        self.visszaBtn_copy.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn_copy.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_10.Add(self.visszaBtn_copy, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panel_9 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_9, 1, wx.EXPAND, 0)

        sizer_11 = wx.BoxSizer(wx.VERTICAL)

        self.panel_10 = wx.Panel(self.panel_9, wx.ID_ANY)
        sizer_11.Add(self.panel_10, 1, wx.EXPAND, 0)

        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_3 = wx.StaticBitmap(self.panel_10, wx.ID_ANY, wx.Bitmap("C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/projektek/covidStat/images/walkSmall.gif", wx.BITMAP_TYPE_ANY))
        sizer_12.Add(bitmap_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.panel_11 = wx.Panel(self.panel_9, wx.ID_ANY)
        sizer_11.Add(self.panel_11, 1, wx.EXPAND, 0)

        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)

        label_3 = wx.StaticText(self.panel_11, wx.ID_ANY, u"Eljött Dionüsszosz Diadalnapja!", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Segoe Print"))
        label_3.Wrap(300)
        sizer_13.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10)

        self.panel_12 = wx.Panel(self.panel_9, wx.ID_ANY)
        sizer_11.Add(self.panel_12, 1, wx.EXPAND, 0)

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)

        self.visszaBtn_copy_1 = wx.Button(self.panel_12, wx.ID_ANY, "Rohanok is a boltba...", style=wx.BU_AUTODRAW)
        self.visszaBtn_copy_1.SetBackgroundColour(wx.Colour(212, 229, 255))
        self.visszaBtn_copy_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "MV Boli"))
        sizer_14.Add(self.visszaBtn_copy_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.panel_12.SetSizer(sizer_14)

        self.panel_11.SetSizer(sizer_13)

        self.panel_10.SetSizer(sizer_12)

        self.panel_9.SetSizer(sizer_11)

        self.panel_8.SetSizer(sizer_10)

        self.panel_7.SetSizer(sizer_9)

        self.panel_6.SetSizer(sizer_8)

        self.panel_5.SetSizer(sizer_5)

        self.panel_4.SetSizer(sizer_6)

        self.panel_3.SetSizer(sizer_7)

        self.panel_2.SetSizer(sizer_4)

        self.panel_1.SetSizer(sizer_3)

        self.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class MyFrameMondjam

class MyFrameMutassam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameMutassam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((647, 469))
        self.SetTitle("Quarantine CountDown")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\projektek\\covidStat\\images\\maskIcon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(110, 149, 195))

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.grid_1.CreateGrid(10, 0)
        self.grid_1.SetRowLabelSize(5)
        self.grid_1.SetColLabelSize(0)
        self.grid_1.EnableEditing(0)
        sizer_2.Add(self.grid_1, 1, wx.EXPAND, 0)

        sizer_2.Add((20, 20), 0, 0, 0)

        self.visszaBtn = wx.Button(self.panel_1, wx.ID_ANY, "Vissza")
        sizer_2.Add(self.visszaBtn, 0, 0, 0)

        sizer_2.Add((0, 0), 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyFrameMutassam

class MyApp(wx.App):
    def OnInit(self):
        
        self.frame = MyFrameFo(None, wx.ID_ANY, "")
        self.frame2 = MyFrameMondjam(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
        return True
   
# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
