import wx
from FoglalasFrame import FoglalasFrame
import feladat_fog

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((700, 550))
        self.SetTitle("frame")

        self.paciensekNevei=[f'{szemely.nevV} {szemely.nevK}' for szemely in feladat_fog.szemelyek]
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"új foglalás felvitele", "")
        self.Bind(wx.EVT_MENU, self.uj_foglalas_listaba, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"mentés fájlba", "")
        self.Bind(wx.EVT_MENU, self.menu_foglalas_mentes, item)
        self.frame_menubar.Append(wxglade_tmp_menu, u"Foglalások")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Új páciens", "")
        self.Bind(wx.EVT_MENU, self.uj_paciens_listaba, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"mentés fájlba", "")
        self.Bind(wx.EVT_MENU, self.menu_mentes_fajlba, item)
        self.frame_menubar.Append(wxglade_tmp_menu, u"Páciensek")
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.Append(wxglade_tmp_menu, u"Kilépés")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1.SetMinimumPaneSize(20)
        sizer_2.Add(self.window_1, 1, wx.EXPAND, 0)

        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, u"Páciensek", style=wx.ALIGN_LEFT)
        label_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_3.Add(label_1, 1, wx.BOTTOM | wx.TOP, 15)

        self.combo_box_paciens = wx.ComboBox(self.window_1_pane_1, wx.ID_ANY, choices=self.paciensekNevei, style=wx.CB_DROPDOWN)
        sizer_3.Add(self.combo_box_paciens, 1, wx.ALL | wx.EXPAND, 10)

        label_2 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, u"Kezelések")
        label_2.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_3.Add(label_2, 1, wx.BOTTOM | wx.TOP, 15)

        self.combo_box_kezelesek = wx.ComboBox(self.window_1_pane_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        sizer_3.Add(self.combo_box_kezelesek, 1, wx.ALL | wx.EXPAND, 10)

        label_3 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, "Orvosok")
        label_3.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_3.Add(label_3, 1, wx.BOTTOM | wx.TOP, 15)

        self.combo_box_orvosok = wx.ComboBox(self.window_1_pane_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        sizer_3.Add(self.combo_box_orvosok, 1, wx.ALL | wx.EXPAND, 10)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)

        self.btn_foglalas = wx.Button(self.window_1_pane_1, wx.ID_ANY, "Foglalj most!")
        sizer_5.Add(self.btn_foglalas, 0, wx.ALL | wx.SHAPED, 10)

        self.btn_close = wx.BitmapButton(self.window_1_pane_1, wx.ID_ANY, wx.Bitmap("C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/grafikusSzoftver/fogaszat_python/src/fajlok/img/exit_picture.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW | wx.BU_NOTEXT)
        self.btn_close.SetMinSize((100, 100))
        sizer_5.Add(self.btn_close, 0, wx.ALIGN_RIGHT | wx.ALL | wx.FIXED_MINSIZE, 6)

        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        self.panel_textek = wx.Panel(self.window_1_pane_2, wx.ID_ANY, style=wx.BORDER_NONE)
        self.panel_textek.SetBackgroundColour(wx.NullColour)
        sizer_4.Add(self.panel_textek, 1, wx.ALL | wx.EXPAND, 6)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl_kicsoda = wx.TextCtrl(self.panel_textek, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_READONLY)
        self.text_ctrl_kicsoda.Hide()
        sizer_6.Add(self.text_ctrl_kicsoda, 1, wx.ALL | wx.EXPAND, 10)

        self.text_ctrl_mit = wx.TextCtrl(self.panel_textek, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_READONLY)
        self.text_ctrl_mit.Hide()
        sizer_6.Add(self.text_ctrl_mit, 1, wx.ALL | wx.EXPAND, 10)

        self.text_ctrl_kinek = wx.TextCtrl(self.panel_textek, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_READONLY)
        self.text_ctrl_kinek.Hide()
        sizer_6.Add(self.text_ctrl_kinek, 1, wx.ALL | wx.EXPAND, 10)

        bitmap_1 = wx.StaticBitmap(self.window_1_pane_2, wx.ID_ANY, wx.Bitmap("C:/Users/Szalamandra/Documents/szf/egressy/python/wxgladesprogik/wxglade_env/grafikusSzoftver/fogaszat_python/src/fajlok/img/fog.jpg", wx.BITMAP_TYPE_ANY), style=wx.BORDER_SUNKEN | wx.FULL_REPAINT_ON_RESIZE)
        bitmap_1.SetMinSize((300, 200))
        sizer_4.Add(bitmap_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL  | wx.FIXED_MINSIZE, 6)

        self.panel_textek.SetSizer(sizer_6)

        self.window_1_pane_2.SetSizer(sizer_4)

        self.window_1_pane_1.SetSizer(sizer_3)

        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.click_foglal, self.btn_foglalas)
        self.Bind(wx.EVT_BUTTON, self.click_close, self.btn_close)
        # end wxGlade
        self.foglalasFrame=FoglalasFrame(None, wx.ID_ANY, "")

        


    def uj_foglalas_listaba(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'uj_foglalas_listaba' not implemented!")
        event.Skip()

    def menu_foglalas_mentes(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'menu_foglalas_mentes' not implemented!")
        event.Skip()

    def uj_paciens_listaba(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'uj_paciens_listaba' not implemented!")
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
        print("Event handler 'click_close' not implemented!")
        event.Skip()


    
    def frameValto(self):
        pass
# end of class MyFrame
