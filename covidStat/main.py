#pip install requests, beautifulsoup4, xml-parser

from bs4 import BeautifulSoup
import requests



#interpreter: C:\Users\Szalamandra\Documents\szf\egressy\python\wxgladesprogik\wxglade_env\Scripts\python.exe
URL = "https://news.google.com/covid19/map?hl=hu&gl=HU&ceid=HU%3Ahu&mid=%2Fm%2F03gj2"
#URL="https://news.google.com/covid19/map"

html_text = requests.get(URL).content
soup = BeautifulSoup(html_text, "html.parser")
statData = soup.findAll('div', class_='tIUMlb')
ujNapiData=[]
for napiData in statData:
    if 'strong' in napiData:
        ujNapiData = napiData.append(ujNapiData)
    
#ujFertozottSzam=ujFertozott.find('+')
print(ujNapiData)
