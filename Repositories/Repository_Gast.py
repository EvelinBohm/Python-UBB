from Entities.Gast import Gast


class Repository_Gast:
    def __init__(self, file="data"):
        self.__fName = file
        self.__data = [] # Liste von Gasten
        self.__loadFromFile()#die Daten werden aus der Datei hochgeladen

    @property
    def return_data(self):
        return self.__data

    def add(self, name):#ein neuer Gast wird hinzugefuegt
        self.__data.append(name)
        self.__storeToFile()

    def find(self, name):#fuer die Veraenderung des Nachnamen eines Gastes(der Gast wird in der Datei gesucht)
        for guest in self.__data:
            if name == guest:
                return guest
        return None

    def modify(self, name, new_last):#Veraenderung des Nachnamens

        guest = self.find(name)#Gast wird mit der Funktion find gesucht

        if guest is None:
            raise ValueError("Guest not found.Please add guest to the list")

        modified_name = Gast(guest.first_name, new_last)#Veraederung des Nachnamen

        idx = self.__data.index(guest)
        self.__data.pop(idx)
        self.__data.insert(idx, modified_name)

        self.__storeToFile()#wird in die Datei eingefuegt

    def delete(self, name):#Loesung eines Gastes
        for el in self.__data:#Gast wird gesucht
            if el == name:
                self.__data.remove(el)

        self.__storeToFile()#Aenderung wird in der Datei vorgenommen

    def print_list(self):

        for guest in self.__data:
            return guest

    def __storeToFile(self):#Funktion fuers updaten der Datei
        f = open(self.__fName, 'w')
        for el in self.__data:
            f.write(str(el) + "\n")
        f.close()

    def __loadFromFile(self):#Funktion fuers Lesen der Datei
        f = open(self.__fName, 'r')
        for line in f:
            data = line.strip().split(' ')
            univ = Gast(data[0], data[1])
            self.__data.append(univ)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
