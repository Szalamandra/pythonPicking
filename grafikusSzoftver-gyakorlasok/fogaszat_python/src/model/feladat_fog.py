
from os import path, curdir
from szemely import Szemely
baseFolder = path.abspath(curdir)

"""paciensF = "C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\grafikusSzoftver\\fogaszat_python\\src\\fajlok\\paciensek.txt"
kezelesF = "C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\grafikusSzoftver\\fogaszat_python\\src\\fajlok\\paciensek.txt"
fogorvF = "C:\\Users\\Szalamandra\\Documents\\szf\\egressy\\python\\wxgladesprogik\\wxglade_env\\grafikusSzoftver\\fogaszat_python\\src\\fajlok\\paciensek.txt"
"""
paciensF = path.join(baseFolder, "src\\fajlok\\paciensek.txt")
kezelesF = path.join(baseFolder, "src/fajlok/kezelesek.txt")
fogorvF = path.join(baseFolder, "src/fajlok/fogorvosok.txt")


def szemelyBeolvas(FAJL):
    lista = []
    with open(FAJL, "r", encoding="utf-8") as f:
        for sor in f:
            sor = sor.strip().split()
            lista.append(Szemely(sor[0], sor[1], sor[2]))

    return lista


def listaBeolvas(FAJL):
    lista = []
    with open(FAJL, "r", encoding="utf-8") as f:
        for sor in f:
            sor = sor.strip()
            lista.append(sor)
    return lista


szemelyek = szemelyBeolvas(paciensF)
kezelesek = listaBeolvas(kezelesF)
orvosok = listaBeolvas(fogorvF)
#print(str(orvosok), str(szemelyek), str(kezelesek))