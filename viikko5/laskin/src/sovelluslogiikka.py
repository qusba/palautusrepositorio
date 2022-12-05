class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
    
    def anna_tulos(self):
        return self.tulos

class Summa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote
        self.tila_ennen_komentoa = 0

    def suorita(self):
        self.tila_ennen_komentoa = self.sovellus.anna_tulos()
        return self.sovellus.plus(int(self.syote()))
    
    def kumoa(self):
        return self.tila_ennen_komentoa

class Erotus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote
        self.tila_ennen_komentoa = 0

    def suorita(self):
        self.tila_ennen_komentoa = self.sovellus.anna_tulos()
        return self.sovellus.miinus(int(self.syote()))
    
    def kumoa(self):
        return self.tila_ennen_komentoa

class Nollaus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote
        self.tila_ennen_komentoa = 0

    def suorita(self):
        self.tila_ennen_komentoa = self.sovellus.anna_tulos()
        return self.sovellus.nollaa()
    
    def kumoa(self):
        return self.tila_ennen_komentoa

class Kumoa:
    def __init__(self, sovellus, komentohistoria):
        self.sovellus = sovellus
        self.komentohistoria = komentohistoria

    def suorita(self):
        self.komentohistoria.pop()
        viimeisin_olio = self.komentohistoria[-1]
        return self.sovellus.aseta_arvo(viimeisin_olio.kumoa())