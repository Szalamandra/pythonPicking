class Ered:
    def __init__(self,helyezes, hanyan_ertek_el, sportag, versenyszam):
        self.helyezes=int(helyezes)
        self.hanyan_ertek_el=int(hanyan_ertek_el)
        self.sportag=sportag
        self.versenyszam=versenyszam

    def __str__(self):
        return f"{self.helyezes} {self.hanyan_ertek_el} {self.sportag} {self.versenyszam}\n"

