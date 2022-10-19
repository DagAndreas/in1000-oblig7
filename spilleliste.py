from sang import Sang
#importerer klassen Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
            #lager en liste som blir brukt som en liste hvor vi legger til sang
            #objekter senere.
        self._listeNavn = listenavn
            #lagrer navnet som brukeren kaller spillelisten.

    def __str__(self):
        print(self._listenavn)
            #definerer hva spillelisten blir kalt hvis den blir printet.

    def lesFraFil(self, filnavn):
        sangFil = open(filnavn)
            #åpner filen som brukeren bruker som argument.
        for sang in sangFil:
            alleData = sang.strip().split(";")
                #fjerner unødvendig støy fra filen, og splitter
                #artist og tittel. Så lagres det som en liste kalt "alleData"
            self._sanger.append(Sang(alleData[1], alleData[0]))
                #lager sangobjekter, og legger de til i spillelisten
                #self._sanger

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()
                #spiller av alle objektene i listen self._sanger

    def spillSang(self, valgtSang):
        valgtSang.spill()
            #printer valgtSang sin artist og sangtittel

    def leggTilSang(self, valgtSang):
        self._sanger.append(valgtSang)
            #legger til et sangobjekt

    def finnSang(self, sangtittel):
        for sang in self._sanger:
            #leter etter sangtittel i listen self._sanger
            if sang.sjekkTittel(sangtittel):
                #hvis sangen er i listen, returneres sangobjektet.
                return sang
        return None

    def hentArtistUtvalg(self, artist):
        artistUtvalg = []
        for sang in self._sanger:
            if sang.sjekkArtist(artist):
                #hvis sjekkartist er True vil sangen legges til i
                #artistUtvalg listen.
                artistUtvalg.append(sang)
        return artistUtvalg
            #sender tilbake en liste med objekter hvor artisten er det samme.

    def fjernSang(self, sang):
        for element in self._sanger:
            for musikk in self._sanger:
                #ittererer gjennom alle objektene flere ganger, for å forsikres
                #om at alle objekter fjernes.
                if str(musikk) == str(sang):
                    #hvis det er samme artist og tittel på sangen: fjern den
                    self._sanger.remove(musikk)

    def printSanger(self):
        #metode som kan brukes for å hente alle sangene i spillelisten
        #uten å spille dem av.
        for sang in self._sanger:
            print(sang)
            #print(sang) henter __str__ til sangobjektet
