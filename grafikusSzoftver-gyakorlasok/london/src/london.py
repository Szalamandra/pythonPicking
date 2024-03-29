#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri May 14 13:16:50 2021
#

import wx
import london_feladat

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Confirm")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, u"Biztosan jav�tani akarja?", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_3.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 30)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()

        self.Bind(wx.EVT_CLOSE, self.close_x, self)
        # end wxGlade

    def close_x(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'close_x' not implemented!")
        event.Skip()

# end of class MyDialog

class MyDialog1(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog_1")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())

        self.Layout()
        # end wxGlade

# end of class MyDialog1
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((424, 455))
        self.SetTitle("London")

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetMinSize((384, 367))
        sizer_1.Add(self.panel_1, 0, 0, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "London")
        label_1.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 5)

        self.javit_btn = wx.Button(self.panel_1, wx.ID_ANY, u"jav�t")
        sizer_3.Add(self.javit_btn, 0, wx.LEFT | wx.RIGHT, 45)

        self.nevjegy_btn = wx.Button(self.panel_1, wx.ID_ANY, u"N�vjegy", style=wx.BU_AUTODRAW)
        sizer_3.Add(self.nevjegy_btn, 1, wx.LEFT | wx.RIGHT, 45)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "4.elso helyezettek")
        sizer_4.Add(label_2, 1, wx.BOTTOM | wx.LEFT | wx.TOP, 10)

        self.text_elso_hely = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_4.Add(self.text_elso_hely, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 10)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "5.helyezettek")
        sizer_5.Add(label_3, 1, wx.BOTTOM | wx.LEFT | wx.TOP, 10)

        self.text_helyezettek = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_5.Add(self.text_helyezettek, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 10)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, u"6. egy�ni helyezettek")
        sizer_6.Add(label_4, 1, wx.BOTTOM | wx.LEFT | wx.TOP, 10)

        self.list_text_egyszeri_vers = wx.ListBox(self.panel_1, wx.ID_ANY, choices=["choice 1"])
        sizer_6.Add(self.list_text_egyszeri_vers, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 10)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, u"7.sport�gak")
        sizer_7.Add(label_5, 1, wx.BOTTOM | wx.LEFT | wx.TOP, 10)

        self.list_text_sportagak = wx.ListBox(self.panel_1, wx.ID_ANY, choices=["choice 1"])
        sizer_7.Add(self.list_text_sportagak, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 10)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_8, 1, wx.EXPAND, 0)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, u"8.legt\u00f6bbet r\u00e9sztvev\u0151")
        sizer_8.Add(label_6, 1, wx.BOTTOM | wx.LEFT | wx.TOP, 10)

        self.text_legtobb = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_8.Add(self.text_legtobb, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 10)

        self.feladatok_btn = wx.Button(self.panel_1, wx.ID_ANY, "feladatok")
        sizer_2.Add(self.feladatok_btn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 15)

        self.panel_1.SetSizer(sizer_2)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.click_javit, self.javit_btn)
        self.Bind(wx.EVT_BUTTON, self.click_nevjegy, self.nevjegy_btn)
        self.Bind(wx.EVT_BUTTON, self.click_feladat, self.feladatok_btn)
        # end wxGlade

    def click_javit(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_javit' not implemented!")
        event.Skip()

    def click_nevjegy(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_nevjegy' not implemented!")
        event.Skip()

    def click_javit(self, event):  # wxGlade: MyFrame.<event_handler>
        london_feladat.javit(london_feladat.eredmenyek, london_feladat.KIIRF)
        event.Skip()

    def click_nevjegy(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_nevjegy' not implemented!")
        event.Skip()

    def click_feladat(self, event):
        self.kiIrdbEgyeniek()
        self.kiirElsoHelyek()
        self.kiirHelyezettek()
        self.kiirSportagak()
        event.Skip()

    def kiirElsoHelyek(self):
        eredmenyek = london_feladat.eredmenyek
        db = london_feladat.elsoHelyezett(eredmenyek)
        self.text_elso_hely.SetLabelText(str(db))

    def kiirHelyezettek(self):
        eredmenyek = london_feladat.eredmenyek
        db = london_feladat.dbHelyezesek(eredmenyek)
        for key, value in db.items():
            self.text_helyezettek.SetLabelText(f"helyezes: {key} hányan: {value} \n")

    def kiIrdbEgyeniek(self):
        eredmenyek = london_feladat.eredmenyek
        dictDb = london_feladat.dbEgyeniek(eredmenyek)
        kiirLista = []
        for key, value in dictDb.items():
            kiirLista.append(f"helyezes: {key} hányan: {value} \n")

        self.list_text_egyszeri_vers.Clear()
        self.list_text_egyszeri_vers.Append(kiirLista)

    def kiirSportagak(self):
        eredmeny = self.sportagak()
        self.list_text_sportagak.Clear()
        for ered in eredmeny:
            self.list_text_sportagak.Append(str(ered))

    def sportagak(self):
        eredmenyek = london_feladat.eredmenyek
        sportagak = set([ered.sportag for ered in eredmenyek])
        return sportagak

    def legtobbResztvevoCsoport(self):
        eredmenyek = london_feladat.eredmenyek
        dictSportResztVevo = {}
        sportagak = list(set([ered.sportag for ered in eredmenyek]))

        for sportag in sportagak:
            
            for ered in eredmenyek:
                if (
                    ered.sportag == sportag
                    and dictSportResztVevo.get(sportag, "nem van ilyen")
                    in dictSportResztVevo.values()
                ):
                    dictSportResztVevo[str(sportag)] += ered.hanyan_ertek_el
                else:
                    dictSportResztVevo[str(sportag)] = ered.hanyan_ertek_el
        print(dictSportResztVevo)


    def click_feladat(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'click_feladat' not implemented!")
        event.Skip()
# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.frame.legtobbResztvevoCsoport()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
