import wx
#from views.MyFrameMutassam import MyFrameMutassam
from models.conzolosCovidStat import FoCucc
from models.conzolosCovidStat import NapiAdat


class mutassamController:
    def __init__(self, frame):
        self.frame = frame
        self.model = FoCucc()
        #self.frame.grid_tabla.SetCellValue(0, 0, "mama")
        self.tabla = self.frame.grid_tabla
        self.tablaFeltolt()
        #adatkiiras a tablazatba
        #https://wxpython.org/Phoenix/docs/html/wx.grid.Grid.html#wx-grid-grid    tablazatba az adatot a focucctol

    def tablaFeltolt(self):
        adatObjLista = self.model.adatOlvasas()

        for i in range(5):
            self.frame.grid_tabla.SetCellValue(i, 0, str(adatObjLista[i].ujFertozott))
            self.frame.grid_tabla.SetCellValue(i, 1, str(adatObjLista[i].napiHalott))

