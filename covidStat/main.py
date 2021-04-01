#pip install requests, beautifulsoup4, xml-parser

#from bs4 import BeautifulSoup
#import requests

import bs4 as bs
import urllib.request
from datetime import datetime


#interpreter: C:\Users\Szalamandra\Documents\szf\egressy\python\wxgladesprogik\wxglade_env\Scripts\python.exe
URL = "https://news.google.com/covid19/map?hl=hu&gl=HU&ceid=HU%3Ahu&mid=%2Fm%2F03gj2"
#URL="https://news.google.com/covid19/map"

#html_text = requests.get(URL).content  ez akkor ha csak a requestset importalom
class FoCucc:
    FAJL = "mentettTestData.txt"
    FAJLOLVASNI="mentettData.txt"
    def fajlNyitasFelulIrasra():
        with open((FoCucc.FAJL), "r", encoding="utf-8") as fr:
            fr = fr.read().replace("\n", ":").split(":")
            for x in fr[:-5]:
                az, ujF, ujH,mN =fr[-5], fr[-4], fr[-3], fr[-1]
                utsoNapiAdat = NapiAdat(az, ujF, ujH, mN)
            print(utsoNapiAdat.maiNapVan)
            return utsoNapiAdat.maiNapVan

    def adatIras(fajlNyitasFelulIrasra = None, obj=None):
        if obj == None:
            raise Exception
            print("vm hiba az adatlekérésben")
        #print("fajlolvassasra: "+str(fajlNyitasFelulIrasra)+ "obj: "+str(obj))
        if fajlNyitasFelulIrasra == None:
            fajlNyitasFelulIrasra = True
        if fajlNyitasFelulIrasra == True:
            obj.felulIras(obj)
            print("felülírtam")
        else:
            obj.mentes(obj)
            print("mentettem")
    

            #return utsoNapiAdat.maiNapVan
    #tablazathoz
    def adatOlvasas():
        objectList=[]
        with open(FoCucc.FAJLOLVASNI, 'rt', encoding='utf-8') as fr:
            lines = fr.readlines()
            #utolsó 5 sorral akarok foglalkozni:
            ujLinesReverse = lines.copy()
            ujLinesReverse = ujLinesReverse[-1:-6:-1]
            for lines in range(5):
                az, nF, nH, nD, mN = ujLinesReverse[lines].replace('\n', '').split(':')
                uj = NapiAdat(az, nF, nH, mN)
                #print(uj)
                objectList.append(uj)

            #print(str(objectList))
            return objectList
    #tablazathoz majd:        
    def kiIrFertozottek(objList):
        for i in range(5):
            print(objList[i].ujFertozott)
    def kiIrHalottak(objList):
        for i in range(5):
            print(objList[i].napiHalott)
    #ertekeles
    def ertekeles(objList):
        szamolo=0
        for i in range(5):
            if int(objList[i].napiHalott)<100: szamolo+=1
        if szamolo == 5: print("Eljött az ünneplés diadala!")
        elif szamolo > 0 and szamolo < 5: print("Lassan indulnék a boltba...")
        else: print("Sajnos még nyaral Dionüszosz...")


        

class NapiAdat:
    COUNTER = 0
    maiNap=datetime.now()

    def __init__(self, az, ujFertozott, napiHalott, mentesNap):
        self.ujFertozott = ujFertozott
        self.napiHalott = napiHalott
        self.az = az
        az=NapiAdat.COUNTER+1
        self.mentesNap=mentesNap
        self.maiNapVan= str(NapiAdat.maiNap.day)==self.mentesNap
        
    def __str__(self):
        return f"{self.az}:{self.ujFertozott}:{self.napiHalott}:{self.mainapStr()}:{self.mentesNap}"

    def mainapStr(self):
        return f"{self.maiNap.year} {self.maiNap.month} {self.maiNap.day}"
    

    #NapiAdat object-et adja vissza
    def napiAdatKeres():           
        html_text=urllib.request.urlopen(URL)
        soup = bs.BeautifulSoup(html_text, 'html.parser')
        statDataList = soup.findAll('div', class_='tIUMlb')
        napiDataList = []
        for napi in statDataList:
            uj = napi.find('strong')
            napiDataList.append(uj)
        #print(napiDataList)

        for d in range(1):
            ujFertozott = str(napiDataList[0])[8:-9]        #.strip("<strong>") de nemjo a zarotag miatt   # str mert a type is bs4 class element
            napiHalott = str(napiDataList[1])[8:-9] 
        #print(f"{napiHalott} es a fert {ujFertozott}")
        ma = str(NapiAdat.maiNap.day)
        az=NapiAdat.COUNTER
        ujNapi = NapiAdat(az,ujFertozott, napiHalott, ma )
        return ujNapi
    
    def mentes(self,ujObject=None):
        if ujObject == None:
            raise Exception
        else:    
            with open(FoCucc.FAJL, "a", encoding="UTF-8") as fa:
                line = ":".join(["\n"+str(ujObject.az), ujObject.ujFertozott, ujObject.napiHalott, ujObject.mainapStr(), str(ujObject.mentesNap)])
                fa.write(line)
                fa.close()
                #return utsoNapiAdat.maiNapVan

    def felulIras(self, ujObject=None):
        if ujObject == None:
            raise Exception
        else:
            with open(FoCucc.FAJL, "a+", encoding="UTF-8") as fw:
                fw.seek(0)
                lines = fw.readlines()
                utsosorCharSzam=len(lines[len(lines) - 1])
                utsoSor = lines[len(lines) - 1].split(":")  #listat ad vissza az utsosor elemeivel
                utsoSor[0]=ujObject.az
                utsoSor[1] = ujObject.ujFertozott
                utsoSor[2] = ujObject.napiHalott
                regiObject=NapiAdat(utsoSor[0],utsoSor[1],utsoSor[2],ujObject.mentesNap)

                print('regi: {0}, utsosor: {1}'.format(regiObject, utsoSor))
                fw.seek(regiObject.az)
                fw.write(str(regiObject))

                fw.close()


#obj=NapiAdat.napiAdatKeres()
#FoCucc.adatIras(FoCucc.fajlNyitasFelulIrasra(), obj)
adatObjLista = FoCucc.adatOlvasas()
#FoCucc.kiIrFertozottek(adatObjLista)
#FoCucc.kiIrHalottak(adatObjLista)
FoCucc.ertekeles(adatObjLista)