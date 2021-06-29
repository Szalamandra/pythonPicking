class Foglalas:
    def __init__(self,nev,kezeles, orvos):
        self.nev=nev
        self.kezeles=kezeles
        self.orvos=orvos

    def __str__(self):
        return f"{self.nev};{self.kezeles};{self.orvos}\n"