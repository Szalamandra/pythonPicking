from ered import Ered

FAJL = "london.txt"
KIIRF = "london2.txt"


def adatBeker(FAJL):
    lista = []
    adatok = []
    with open(FAJL, "r", encoding="utf-8") as f:
        elso = f.readline()
        for sor in f:
            sor = sor.strip()
            adatok.append(sor)
    utso = adatok.pop()
    for sor in adatok:
        sor = sor.split()
        lista.append(Ered(sor[0], sor[1], sor[2], sor[3]))
    return lista


def javit(eredmenyek, KIIRF="london2.txt"):
    with open(KIIRF, "w", encoding="utf-8") as f:
        for ered in eredmenyek:
            if ered.sportag.lower() == "cselgancs":
                ered.sportag = "Cselgáncs"

            f.write(str(ered))
    f.close()


def elsoHelyezett(eredmenyek):
    db = 0
    for ered in eredmenyek:
        if ered.helyezes == 1:
            db += ered.helyezes * ered.hanyan_ertek_el
    #print(str(db))
    return db


def dbHelyezesek(eredmenyek):
    kisTuplek = [(ered.helyezes, ered.hanyan_ertek_el) for ered in eredmenyek]
    dictDb = {}

    for tup in kisTuplek:
        if tup[0] in dictDb:
            dictDb[tup[0]] += tup[1]
        else:
            dictDb[tup[0]] = tup[1]
    for key, value in dictDb.items():
        print(f"helyezes: {key} hányan: {value} ")
    return dictDb

def dbEgyeniek(eredmenyek):
    kisTuplek = [(ered.helyezes, ered.hanyan_ertek_el) for ered in eredmenyek]
    dictDb = {}
    j = 0

    while kisTuplek[j][0] < 4:
        if kisTuplek[j][0] in dictDb and kisTuplek[j][1] == 1:
            dictDb[kisTuplek[j][0]] += 1
        else:
            dictDb[kisTuplek[j][0]] = 1
        j += 1
    #for key, value in dictDb.items():
    #   print(f"helyezes: {key} hányan: {value} ")
    return dictDb



eredmenyek = adatBeker(FAJL)
elsoHelyezett(eredmenyek)
# dbHelyezesek(eredmenyek)
dbEgyeniek(eredmenyek)