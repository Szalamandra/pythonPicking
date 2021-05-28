import wx

# from views.MyFrameMondjam import MyFrameMondjam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mondjamController:
    def __init__(self, frameMondjam):
        self.frame = frameMondjam
        self.model = FoCucc()

        adatObjLista = self.model.adatOlvasas()
        ertek = self.model.ertekeles(adatObjLista)  # 0,1,2
        self.on_init_mondjam(ertek)

    def on_init_mondjam(self, ertek):

        print("ertek " + str(ertek))
        szam = self.panelValto(ertek)
        self.panelMutato(szam)
        # print(f"benne vagyok a controllelben eertek: {str(ertek)}")

    # 0-2 ig rendelek a panelekhez szamot, Z ertekelesben kapom hogy melyik jelenjen meg
    # dictszám itt félreérthető, mostmár ez lista, de nem írtam át
    def panelValto(self, panelSzam):
        dictSzamok = [0]
        # animaciok lejatszasa panelszam alapjan,  mert különben vibrál a kép
        dictCtrlAnim = {
            self.frame.panelFo_ertekelesJo: self.frame.ctrl2,
            self.frame.panelFo_ertekelesKozep: self.frame.ctrl1,
            self.frame.panelFo_ertekelesRossz: self.frame.ctrl,
        }

        if panelSzam == 2:

            dictSzamok[0] = [
                self.frame.panelFo_ertekelesJo,
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesRossz,
            ]
            # dictSzamok.append(self.frame.panelFo_ertekelesJo)
            # dictSzamok.insert(1,self.frame.panelFo_ertekelesKozep)
            # dictSzamok.insert(2,self.frame.panelFo_ertekelesRossz)
            dictCtrlAnim[self.frame.panelFo_ertekelesJo].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesJo].Play()
        elif panelSzam == 1:
            dictSzamok[0] = [
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesRossz,
                self.frame.panelFo_ertekelesJo,
            ]

            dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Play()
        else:

            dictSzamok[0] = [
                self.frame.panelFo_ertekelesRossz,
                self.frame.panelFo_ertekelesKozep,
                self.frame.panelFo_ertekelesJo,
            ]

            dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Show()
            dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Play()

        for i in dictSzamok:
            print(type(i))
        return dictSzamok

    def panelMutato(self, dictSzam):

        dictSzam[0][0].Show()
        dictSzam[0][1].Hide()
        dictSzam[0][2].Hide()

    # ez a rész dict-el de ezt átírom listára
    """def panelValto(self, panelSzam):
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
                dictSzamok[0] = [
                    self.frame.panelFo_ertekelesKozep,
                    self.frame.panelFo_ertekelesRossz,
                    self.frame.panelFo_ertekelesJo,
                ]
                dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Show()
                dictCtrlAnim[self.frame.panelFo_ertekelesKozep].Play()
            else:
                dictSzamok[0] = [
                    self.frame.panelFo_ertekelesRossz,
                    self.frame.panelFo_ertekelesKozep,
                    self.frame.panelFo_ertekelesJo,
                ]
                dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Show()
                dictCtrlAnim[self.frame.panelFo_ertekelesRossz].Play()

            self.panelMutato(dictSzamok)

    def panelMutato(self, dictSzam):
        
        for val in dictSzam:
            #print(val[0], val[1])
            val[0].Show()
            val[1].Hide()
            val[2].Hide()
        """
