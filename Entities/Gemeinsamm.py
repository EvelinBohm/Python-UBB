class Gemeinsamm:
    def __init__(self, gaste_Reservierung, zimmer_Reservierung, ankunft_Zeit, abfahrt_Zeit):  # fon = frei oder nicht #Meerblick oder nicht
        self.__gaste_Reservierung = gaste_Reservierung
        self.__zimmer_Reservierung = zimmer_Reservierung
        self.__ankunft_Zeit = ankunft_Zeit
        self.__abfahrt_Zeit = abfahrt_Zeit

    def __str__(self):
        return "{} {} {} {}".format(self.__gaste_Reservierung, self.__zimmer_Reservierung, self.__ankunft_Zeit, self.__abfahrt_Zeit)


    @property
    def gaste_Reservierung(self):
        return self.__gaste_Reservierung

    @gaste_Reservierung.setter
    def gaste_Reservierung(self, gaste_Reservierung):
        self.__gaste_Reservierung = gaste_Reservierung

    @property
    def zimmer_Reservierung(self):
        return self.__zimmer_Reservierung

    @zimmer_Reservierung.setter
    def zimmer_Reservierung(self, zimmer_Reservierung):
        self.__zimmer_Reservierung = zimmer_Reservierung

    @property
    def ankunft_Zeit(self):
        return self.__ankunft_Zeit

    @ankunft_Zeit.setter
    def ankunft_Zeit(self, ankunft_Zeit):
        self.__ankunft_Zeit = ankunft_Zeit

    @property
    def abfahrt_Zeit(self):
        return self.__abfahrt_Zeit

    @abfahrt_Zeit.setter
    def abfahrt_Zeit(self, abfahrt_Zeit):
        self.__abfahrt_Zeit = abfahrt_Zeit
