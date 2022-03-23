from Entities.Zimmer import Zimmer


class ReposRoom:
    def __init__(self, file="rooms"):
        self.__fName = file
        self.__list_room = []# Liste von Zimmern
        self.__loadFromFile()#die Daten werden aus der Datei hochgeladen

    @property
    def room_list(self):
        return self.__list_room

    def add(self, room):#ein neueres Zimmer wird hinzugefuegt

        for r in self.__list_room:
            if room.nummer==r.nummer:
                raise ValueError("Room already exists")
        else:
            self.__list_room.append(room)
            self.__storeToFile()

    def find(self, room_number):#fuer die Veraenderung des Preises eines Zimmers(die Zimmernumer wird in der Datei gesucht)
        for room in self.__list_room:
            if room.nummer == room_number:
                return room
        return None

    def modify_price(self, room_nr, new_price):#Veraenderung des Preises

        room = self.find(room_nr)#Zimmer wird gesucht

        if room is None:
            raise ValueError("Room not found.Please add room to the list")

        modified_price = Zimmer(room.nummer, room.anzahl_gaste, new_price, room.farbe, room.fon, room.mon)#Zimmer wird veraendert
        idx = self.__list_room.index(room)
        self.__list_room.pop(idx)
        self.__list_room.insert(idx, modified_price)

        self.__storeToFile()#Aenderung wird in der Datei vorgenommen

    def delete_room(self, room_nr):#Loesung eines Zimmers
        for room in self.__list_room:#Zimmer wird gesucht
           if(room.nummer==room_nr):
               self.__list_room.remove(room)
        self.__storeToFile()#Aenderung wird in der Datei vorgenommen

    def print_list(self):#fuer Anzeugen der Zimmer
        for room in self.__list_room:
            return room

    def __loadFromFile(self):#Funktion fuers Lesen der Datei
        f = open(self.__fName, 'r')
        for line in f:
            room = line.strip().split(' ')
            univ = Zimmer(room[0], room[1], room[2], room[3], room[4], room[5])
            self.__list_room.append(univ)

    def __storeToFile(self):#Funtion fuers updaten der Datei
        f = open(self.__fName, 'w')
        for el in self.__list_room:
            f.write(str(el) + "\n")
        f.close()#die Datei wird geschlossen
