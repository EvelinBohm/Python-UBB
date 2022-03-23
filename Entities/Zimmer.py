class Zimmer:
    def __init__(self, nummer, anzahl_gaste, preis, farbe, fon, mon):  # fon = frei oder nicht #Meerblick oder nicht
        self.__nummer = nummer
        self.__anzahl_gaste = anzahl_gaste
        self.__preis = preis
        self.__farbe = farbe
        self.__fon = fon
        self.__mon = mon

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.nummer,
                                                                                              self.anzahl_gaste,
                                                                                              self.preis, self.farbe,
                                                                                              self.fon, self.mon)


    def __eq__(self, other):
        return self.__nummer == other.__nummer or self.__mon==other.__mon
    def __le__(self, other):
        return  self.__preis<=other.__preis
    def __ge__(self,other):
        return self.__preis >= other.__preis
    def __gt__(self, other):
        return self.__anzahl_gaste>other.anzahl_gaste




    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, nummer):
        self.__nummer = nummer

    @property
    def anzahl_gaste(self):
        return self.__anzahl_gaste

    @anzahl_gaste.setter
    def anzahl_gaste(self, anzahl_gaste):
        self.__anzahl_gaste = anzahl_gaste

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, preis):
        self.__preis = preis

    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, farbe):
        self.__farbe = farbe

    @property
    def fon(self):
        return self.__fon

    @fon.setter
    def fon(self, fon):
        self.__fon = fon

    @property
    def mon(self):
        return self.__mon

    @mon.setter
    def mon(self, mon):
        self.__mon = mon
