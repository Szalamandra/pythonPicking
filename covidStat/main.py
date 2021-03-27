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
    FAJL = "mentettData.txt"
    
    def fajlNyitasOlvasasVagyIras():
        with open((FoCucc.FAJL), "r", encoding="utf-8") as fr:
            fr = fr.read().replace("\n", ":").split(":")
            for x in fr[:-4]:
                ujF, ujH,mN = fr[-4], fr[-3], fr[-1]
                utsoNapiAdat = NapiAdat(ujF, ujH, mN)
            #return utsoNapiAdat.maiNapVan
        if (utsoNapiAdat.maiNap):
            mentes(utsoNapiAdat)
        else:
            felulIras(utsoNapiAdat)
    
    def mentes(ujObject):
        ujObject=NapiAdat.napiAdatKeres()
        with open(FAJL, "a", encoding="UTF-8") as fa:
            line = ":".join(ujObject.ujFertozott, ujObject.napiHalott, ujObject.maiNap, ujObject.mentesNap)
            fa.write(line)
            fa.close()
            #return utsoNapiAdat.maiNapVan

    def felulIras(ujObject):
        ujObject=NapiAdat.napiAdatKeres()
        with open(FAJL, "w", encoding="UTF-8") as fw:
            fr = fr.read().replace("\n", ":").split(":")
            for x in fr[:-4]:
                fr[-4] = ujObject.ujFertozott
                fr[-3] = ujObject.napiHalott
            fr.write()
            fr.close()
            #return utsoNapiAdat.maiNapVan

        

class NapiAdat:
    COUNTER = 0
    maiNap=datetime.now()

    def __init__(self, ujFertozott, napiHalott, mentesNap):
        self.ujFertozott = ujFertozott
        self.napiHalott = napiHalott
        self.COUNTER += 1
        self.mentesNap=mentesNap
        self.maiNapVan= int(NapiAdat.maiNap.day)==int(self.mentesNap)
        
    def __str__(self):
        return f"{self.COUNTER}:{self.ujFertozott}:{self.napiHalott}:{self.mainapStr()}:{self.mentesNap}"

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

        ujNapi = NapiAdat(ujFertozott, napiHalott)
        return ujNapi



#NapiAdat.napiAdatKeres()
FoCucc.fajlNyitasOlvasasVagyIras()