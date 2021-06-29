class Foglalas:
    def __init__(self, nev, szoba, szamVendeg):
        self.nev=nev
        self.szoba=szoba 
        self.szamVendeg=szamVendeg


    def __str__(self):
        return f'{self.nev} {self.szoba} {self.szamVendeg}'