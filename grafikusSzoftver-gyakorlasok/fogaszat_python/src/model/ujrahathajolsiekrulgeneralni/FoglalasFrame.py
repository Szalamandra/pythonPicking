# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sun May 16 22:16:21 2021
#

import wx
import feladat_fog

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class FoglalasFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((758, 600))
        self.SetTitle(u"Foglalások")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\grafikusSzoftver\\fogaszat_python\\src\\fajlok\\img\\fog.jpg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.Hide()

        self.panel_foglalas = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.list_box_foglalasok = wx.ListBox(self.panel_foglalas, wx.ID_ANY, choices=[])
        sizer_1.Add(self.list_box_foglalasok, 1, wx.ALL | wx.EXPAND, 6)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.button_beolvas_foglalas = wx.Button(self.panel_foglalas, wx.ID_ANY, u"beolvasás", style=wx.BU_AUTODRAW | wx.BU_EXACTFIT)
        sizer_2.Add(self.button_beolvas_foglalas, 1, wx.ALIGN_CENTER_VERTICAL | wx.FIXED_MINSIZE | wx.LEFT | wx.RIGHT, 45)

        self.button_1 = wx.Button(self.panel_foglalas, wx.ID_ANY, "vissza", style=wx.BU_AUTODRAW | wx.BU_EXACTFIT)
        sizer_2.Add(self.button_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 45)

        self.panel_foglalas.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.click_beolvas_foglalas, self.button_beolvas_foglalas)
        self.Bind(wx.EVT_BUTTON, self.click_vissza, self.button_1)
        # end wxGlade

    def uj_foglalas_listaba(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'uj_foglalas_listaba' not implemented!")
        event.Skip()



    def menu_mentes_fajlba(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'menu_mentes_fajlba' not implemented!")
        event.Skip()

    def menu_kilep(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'menu_kilep' not implemented!")
        event.Skip()

    def click_foglal(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_foglal' not implemented!")
        event.Skip()

    def click_close(self, event):  # wxGlade: MyFrame.<event_handler>
        self.close()
        event.Skip()

    def click_ujpaciens(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_ujpaciens' not implemented!")
        event.Skip()
    def click_vissza(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_vissza' not implemented!")
        event.Skip()
    def click_beolvas_foglalas(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_beolvas_foglalas' not implemented!")
        event.Skip()

    
    """
    def uj_paciens_listaba(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'uj_paciens_listaba' not implemented!")
        event.Skip()
"""
# end of class MyFrame