import wx

# from views.MyFrameMondjam import MyFrameMondjam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mondjamController:
    def __init__(self, frameMondjam):
        self.frame = frameMondjam
        self.model = FoCucc()
        self.on_init_mondjam()

    def on_init_mondjam(self):
        adatObjLista = self.model.adatOlvasas()
        ertek = self.model.ertekeles(adatObjLista)   #0,1,2
        self.panelValto(ertek)

    # 0-2 ig rendelek a panelekhez szamot, Z ertekelesben kapom hogy melyik jelenjen meg
    def panelValto(self, panelSzam):
        dictSzamok = {}
        # animaciok lejatszasa panelszam alapjan,  mert különben vibrál a kép
        dictCtrlAnim = {
            self.frame.panelFo_ertekelesJo: self.frame.ctrl2,
            self.frame.panelFo_ertekelesKozep: self.frame.ctrl1,
            self.frame.panelFo_ertekelesRossz: self.frame.ctrl,
        }

        if panelSzam == 0:
            dictSzamok[0] = [
                self.frame.panelFo_ertekelesJo,
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesRossz,
            ]
            dictCtrlAnim[self.frame.panelFo_ertekelesJo].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesJo].Play()
        elif panelSzam == 1:
            dictSzamok[1] = [
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesRossz,
                self.frame.panelFo_ertekelesJo,
            ]
            dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Play()
        else:
            dictSzamok[2] = [
                self.frame.panelFo_ertekelesRossz,
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesJo,
            ]
            dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Play()

        self.panelMutato(dictSzamok)

    def panelMutato(self, dictSzam):
        for val in dictSzam.values():
            val[0].Show()
            val[1].Hide()
            val[2].Hide()
