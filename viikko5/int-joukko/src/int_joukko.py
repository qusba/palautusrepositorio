
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        
        self.kapasiteetti = self.validaattori(kapasiteetti)
        self.kasvatuskoko = self.validaattori(kasvatuskoko)
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lukumaara = 0
    

    def validaattori(self, alkio):
        if not isinstance(alkio, int) or alkio < 0:
            raise Exception("Virheellinen kapasiteetti tai kasvatuskoko")
        else:
            return alkio


    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        return False


    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lukumaara] = luku
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.taulukko_on_taynna():
                self.pidenna_taulukkoa()


    def taulukko_on_taynna(self):
        return self.alkioiden_lukumaara % len(self.lukujono) == 0


    def pidenna_taulukkoa(self):
        vanha_taulukko = self.lukujono
        self.lukujono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
        self.kopioi_taulukko(vanha_taulukko, self.lukujono)


    def poista(self, luku):
        if self.kuuluu(luku):
            for i in range(len(self.lukujono)):
                if luku == self.lukujono[i]:
                    self.lukujono.pop(i)
                    break
            self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
            return True
        return False


    def kopioi_taulukko(self, kopioitava, uusi_pidennetty):
        for i in range(0, len(kopioitava)):
            uusi_pidennetty[i] = kopioitava[i]


    def mahtavuus(self):
        return self.alkioiden_lukumaara


    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara
        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]
        return taulu
    
    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i]) + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
            tuotos = tuotos + "}"
            return tuotos


class JoukkoOperaatiot:
    def __init__(self, joukko1, joukko2):
        self.lista1 = joukko1.to_int_list()
        self.lista2 = joukko2.to_int_list()

    def yhdiste(self):
        joukko = IntJoukko()

        for i in range(0, len(self.lista1)):
            joukko.lisaa(self.lista1[i])

        for i in range(0, len(self.lista2)):
            joukko.lisaa(self.lista2[i])

        return joukko


    def leikkaus(self):
        joukko = IntJoukko()

        for i in range(0, len(self.lista1)):
            for j in range(0, len(self.lista2)):
                if self.lista1[i] == self.lista2[j]:
                    joukko.lisaa(self.lista2[j])

        return joukko


    def erotus(self):
        joukko = IntJoukko()

        for i in range(0, len(self.lista1)):
            joukko.lisaa(self.lista1[i])

        for i in range(0, len(self.lista2)):
            joukko.poista(self.lista2[i])

        return joukko
