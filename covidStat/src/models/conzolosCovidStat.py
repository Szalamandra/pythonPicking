# pip install requests, beautifulsoup4, xml-parser

# from bs4 import BeautifulSoup
# import requests

import bs4 as bs
import urllib.request
from datetime import datetime
from os import path, curdir
covidStatFolder = path.abspath(curdir)       #from os



# interpreter: C:\Users\Szalamandra\Documents\szf\egressy\python\wxgladesprogik\wxglade_env\Scripts\python.exe
URL = "https://news.google.com/covid19/map?hl=hu&gl=HU&ceid=HU%3Ahu&mid=%2Fm%2F03gj2"
# URL="https://news.google.com/covid19/map"

# html_text = requests.get(URL).content  ez akkor ha csak a requestset importalom
class FoCucc:
    #legyen egy főmethod
    def __init__(self):
        #self.ertekeles(self.adatOlvasas())
        pass
    #FAJL = "mentettData.txt"
    FAJLOLVASNI = path.join(covidStatFolder, "src//models//mentettData.txt")

    #@staticmethod
    #def fajlNyitasFelulIrasra():
    #    with open((FoCucc.FAJL), "r", encoding="utf-8") as fr:
    #        fr = fr.read().replace("\n", ":").split(":")
    #        for x in fr[:-5]:
    #            ujF, ujH, mN = fr[-4], fr[-3], fr[-1]
    #            utsoNapiAdat = NapiAdat(ujF, ujH, mN)
    #        print(utsoNapiAdat.maiNapVan)
    #        return utsoNapiAdat.maiNapVan
    @staticmethod
    def voltEmarMamentes():
        with open(FoCucc.FAJLOLVASNI, "rt", encoding="utf-8") as fr:
            lines = fr.readlines()
            ujLinesReverse = lines.copy()
            ujLinesReverse = ujLinesReverse[-1:-2:-1]
            felvagva = ujLinesReverse[0].split(":")
            mentesnap = felvagva[len(felvagva) - 1]
            d = datetime.today().day
            if mentesnap == str(d):
                print(f"mentesnap {mentesnap} mainap {d}")
                return True
            else:
                print(f"mentesnap {mentesnap} mainap {d}")
                return False
    @staticmethod
    def adatIras(voltEmarMamentes=None):

        if voltEmarMamentes == None:
            voltEmarMamentes = True

        # print("fajlolvassasra: "+str(fajlNyitasFelulIrasra)+ "obj: "+str(obj))
        if voltEmarMamentes == True:
            try:
                obj = NapiAdat.napiAdatkeresObjLetrehozasNelkul()
            except Exception:
                print ("vm hiba az adatlekérésben")
            obj.felulIras(obj)
            print("felülírtam")
        else:
            obj=NapiAdat.napiAdatKeres()
            obj.mentes(obj)
            print("mentettem")

            # return utsoNapiAdat.maiNapVan

    # tablazathoz 
    @staticmethod
    def adatOlvasas():
        objectList = []
        with open(FoCucc.FAJLOLVASNI, "rt", encoding="utf-8") as fr:
            lines = fr.readlines()
            # utolsó 5 sorral akarok foglalkozni:
            ujLinesReverse = lines.copy()
            ujLinesReverse = ujLinesReverse[-1:-6:-1]
            for lines in range(5):
                az, nF, nH, nD, mN = ujLinesReverse[lines].replace("\n", "").split(":")
                # uj = NapiAdat( nF, nH, mN)
                # print(uj)
                objectList.append(NapiAdat(nF, nH, mN))

            # print(str(objectList))
            return objectList



    @staticmethod
    # tablazathoz majd de ezek nem kellettek végül:
    def kiIrFertozottek(objList):
        for i in range(5):
            print(objList[i].ujFertozott)

    @staticmethod
    def kiIrHalottak(objList):
        for i in range(5):
            print(objList[i].napiHalott)

    @staticmethod
    # ertekeles
    def ertekeles(objList):
        szamolo = 0
        for i in range(5):
            if int(objList[i].napiHalott) < 100:
                szamolo += 1
        if szamolo == 5:
            print("Eljött az ünneplés diadala!")
            return 2
        elif szamolo > 0 and szamolo < 5:
            print("Lassan indulnék a boltba...")
            return 1
        else:
            print("Sajnos még nyaral Dionüszosz...")
            return 0

class NapiAdat:
    COUNTER = 0
    maiNap = datetime.now()

    def __init__(self, ujFertozott, napiHalott, mentesNap):
        self.ujFertozott = ujFertozott
        self.napiHalott = napiHalott
        NapiAdat.COUNTER += 1
        self.az = NapiAdat.COUNTER

        self.mentesNap = mentesNap
        self.maiNapVan = str(NapiAdat.maiNap.day) == self.mentesNap

    def __str__(self):
        return f"{self.az}:{self.ujFertozott}:{self.napiHalott}:{self.mainapStr()}:{self.mentesNap}"

    # def __eq__(self, obj):
    #   if self.az == obj.az:
    #      return

    def mainapStr(self):
        return f"{self.maiNap.year} {self.maiNap.month} {self.maiNap.day}"

    # NapiAdat object-et adja vissza
    @staticmethod
    def napiAdatKeres():
        html_text = urllib.request.urlopen(URL)
        soup = bs.BeautifulSoup(html_text, "html.parser")
        statDataList = soup.findAll("div", class_="tIUMlb")
        napiDataList = []
        for napi in statDataList:
            uj = napi.find("strong")
            napiDataList.append(uj)
        # print(napiDataList)
        ujFertozott = str(napiDataList[0])[
            8:-9
        ]  # .strip("<strong>") de nemjo a zarotag miatt   # str mert a type is bs4 class element
        napiHalott = str(napiDataList[1])[8:-9]
        # print(f"{napiHalott} es a fert {ujFertozott}")
        ma = str(NapiAdat.maiNap.day)
        # az=NapiAdat.COUNTER
        ujNapi = NapiAdat(ujFertozott, napiHalott, ma)
        return ujNapi

    @staticmethod
    def napiAdatkeresObjLetrehozasNelkul():
        html_text = urllib.request.urlopen(URL)
        soup = bs.BeautifulSoup(html_text, "html.parser")
        statDataList = soup.findAll("div", class_="tIUMlb")
        napiDataList = []
        for napi in statDataList:
            uj = napi.find("strong")
            napiDataList.append(uj)
        # print(napiDataList)
        ujFertozott = str(napiDataList[0])[8:-9]
        napiHalott = str(napiDataList[1])[8:-9]

        ma = str(NapiAdat.maiNap.day)
        # az=NapiAdat.COUNTER
        ujNapi = NapiAdat(ujFertozott, napiHalott, ma)
        return ujNapi

    def mentes(self, ujObject=None):
        if ujObject == None:
            raise Exception
        else:
            with open(FoCucc.FAJLOLVASNI, "a", encoding="UTF-8") as fa:
                line = ":".join(
                    [
                        "\n" + str(ujObject.az),
                        ujObject.ujFertozott,
                        ujObject.napiHalott,
                        ujObject.mainapStr(),
                        str(ujObject.mentesNap),
                    ]
                )
                fa.write(line)
                fa.close()
                # return utsoNapiAdat.maiNapVan

    def felulIras(self, ujObject=None):
        if ujObject == None:
            raise Exception
        else:
            lines = []
            with open(FoCucc.FAJLOLVASNI, "r+", encoding="UTF-8") as fw:
                fw.seek(0)
                lines = fw.readlines()
                # utsosorCharSzam=len(lines[len(lines) - 1])
                utsoSor = lines.pop()
                print("utso: " + utsoSor)
                # utsoSor = lines[len(lines) - 1].split(":")  #listat ad vissza
                utsoSor = utsoSor.split(":")
                utsoSor[0] = ujObject.az
                utsoSor[1] = ujObject.ujFertozott
                utsoSor[2] = ujObject.napiHalott
                lines.append(ujObject)
                fw.close()
            with open(FoCucc.FAJLOLVASNI, "w+", encoding="UTF-8") as fw:
                for line in range(len(lines)):
                    fw.write(str(lines[line]))
                fw.close()



#FoCucc.adatIras(FoCucc.voltEmarMamentes())
#adatObjLista = FoCucc.adatOlvasas()
#FoCucc.kiIrFertozottek(adatObjLista)
#FoCucc.kiIrHalottak(adatObjLista)
#FoCucc.ertekeles(adatObjLista)
