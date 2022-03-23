class Reservierung:
    def __init__(self, name, anzahl, zimmer, Ankunft_Zeit, Abfahrt_Zeit):
        self.__name = name
        self.__anzahl = anzahl
        self.__zimmer = zimmer
        self.__Ankunft_Zeit = Ankunft_Zeit
        self.__Abfahrt_Zeit = Abfahrt_Zeit

    def __str__(self):
        return "{},{},{},{},{}".format(self.name, self.anzahl, self.zimmer, self.Ankunft_Zeit,
                                             self.__Abfahrt_Zeit)

    def __repr__(self):
        return "{},{},{},{},{}".format(self.name, self.anzahl, self.zimmer, self.Ankunft_Zeit,
                                             self.__Abfahrt_Zeit)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def anzahl(self):
        return self.__anzahl

    @anzahl.setter
    def anzahl(self, anzahl):
        self.__anzahl = anzahl

    @property
    def zimmer(self):
        return self.__zimmer

    @zimmer.setter
    def zimmer(self, zimmer):
        self.__zimmer = zimmer

    @property
    def Ankunft_Zeit(self):
        return self.__Ankunft_Zeit

    @Ankunft_Zeit.setter
    def Ankunft_Zeit(self, Ankunft_Zeit):
        self.__Ankunft_Zeit = Ankunft_Zeit

    @property
    def Abfahrt_Zeit(self):
        return self.__Abfahrt_Zeit

    @Abfahrt_Zeit.setter
    def Abfahrt_Zeit(self, Abfahrt_Zeit):
        self.__Abfahrt_Zeit = Abfahrt_Zeit
