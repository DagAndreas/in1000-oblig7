
class Sang:
    def __init__(self, artist, tittel):
        self._sangArtist = artist
        self._sangTittel = tittel
        #lagrer lokale instansvariabler med parametre artist og tittel
        #for å kunne bruke dem inni et sang-objekt senere.


    def __str__(self):
        return self._sangArtist + ": " + self._sangTittel
        #hvis man skal printe objektet, er det praktisk at det
        #returnerer hvilken sang det er.


    def hentArtistNavnogSangTittel(self):
        return self._sangArtist + ": " + self._sangTittel
        #samme funksjon som __str__, men med annet metodenavn.


    def spill(self):
        print("Spiller " + self._sangArtist + ": " + self._sangTittel)
        #metode for å spille av en sang


    def sjekkVerdi(self, orginal, instansvariabel):
        liste = orginal.lower().split()
        sjekkListe = instansvariabel.lower().split()
        while len(liste) > 0:
            #mens lengden av listen er større enn null:
            if liste[0] in sjekkListe:
            #hvis første element i liste finnes i hele sjekkListe:
                return True
                #returner True
            else:
            #ellers:
                liste.pop(0)
                #fjern første elementet i liste
        return False
        #hvis liste blir tom: returner false.

    def sjekkTittel(self, tittel):
        #skjekker tittel mot sjekkVerdi.
        return self.sjekkVerdi(tittel, self._sangTittel)

    def sjekkArtist(self, artist):
        #skjekker artist mot sjekkVerdi.
        return self.sjekkVerdi(artist, self._sangArtist)

    def sjekkArtistOgTittel(self, navn, tittel):
        #sjekker både artist og tittel med metodene over.
        return self.sjekkArtist(navn) and self.sjekkTittel(tittel)
