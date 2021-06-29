from foglalas import Foglalas
from vendeg import Vendeg
from os import curdir, path
baseF=path.abspath(curdir)
FAJL=path.join(baseF,"src\\fajlok\\foglalasok.txt")
FAJLV=path.join(baseF,"src\\fajlok\\vendeglista1.txt")
FAJLSZ=path.join(baseF,"src\\fajlok\\szobak.txt")

def foglalKeszit(FA):
    lista=[]
    with open(FA, "r", encoding="utf-8") as f:
        for sor in f:
            sor=sor.strip().split()
            lista.append(Foglalas(sor[0], sor[1],sor[2]))
    return lista


def vendegKeszit(FA):
    lista=[]
    with open(FA, "r", encoding="utf-8") as f:
        for sor in f:
            sor=sor.strip().split()
            lista.append(Vendeg(sor[0], sor[1],sor[2]))
    return lista
def szobak(FA):
    lista=[]
    with open(FA, "r", encoding="utf-8") as f:
        for sor in f:
            lista.append(sor.strip())
    return lista



vendegek=vendegKeszit(FAJLV)
foglalasok=foglalKeszit(FAJL)
szobak=szobak(FAJLSZ)
print(vendegek,foglalasok,szobak)
