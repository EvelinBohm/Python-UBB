from Repositories.Repos_rooms import ReposRoom
from Repositories.Repository_Gast import Repository_Gast
from Entities.Reservierung import Reservierung
from datetime import datetime
from tkinter import messagebox


class Repos_gemeinsamm:
    def __init__(self, file='gemeinsam'):
        self.__fName = file
        self.__lst_rez = []  # Liste von Reservirungen
        self.__loadFromFile()  # die Daten werden aus der Datei hochgeladen

    def find_room(self, room_capaciaty):  # passendes Zimmer wird gesucht
        z = ReposRoom()

        for room in z.room_list:

            if (str(room.fon) == "True") and (int(room.anzahl_gaste) == int(
                    room_capaciaty)):  # falls die Anzahl uebereinstimmt wird ein Zimmer angegeben
                return room.nummer
            elif (str(room.fon) == "True") and (int(room.anzahl_gaste) > int(room_capaciaty)):  # falls die Anzhal Gaste grosser ist aber Zimmer mit einer groesseren Kapazitat verfuegbar sind

                def call():#der Gast wird gefragt ob er Einverstanden ist ein Zimmer mit einer grosseren Kapazitat zu reservieren

                    ans = messagebox.askquestion("Sorry",
                                                 "We don't have a room available with the searched capacity,do you want a room with a bigger capacity?")
                    if ans == "yes":
                        return "yes"
                    else:
                        return "no"

                r = call()
                if r == "yes":
                    return room.nummer
                else:
                    return None
            elif room_capaciaty == '':
                return None
        return None#falls keine Zimmer mit einer grosseren Kapazitaet verfuegbar sind

    def find_guest(self, name):#Gast wird gesucht
        g = Repository_Gast()
        for guest in g.return_data:
            if str(guest.first_name + " " + guest.last_name) == str(name):
                return name
        return None

    def add_rez(self, rez):  # ein neue Reservieung wird hinzugefuegt
        r = ReposRoom()
        available_room = self.find_room(rez.anzahl)

        if available_room is None:#falls kein Zimmer zur Verfuegung steht oder der Gast wuenscht kein groesseres Zimmer
            messagebox.showinfo("Sorry", "No available room/Sorry for the inconvenience")
            raise ValueError("No available room/Sorry for the inconvenience ")

        guest = self.find_guest(rez.name)

        if guest is None:#falls Gast nicht in der Liste ist
            messagebox.showerror("No guest found under the given name")
            raise ValueError("Wrong Entry", "No guest found under the given name")


        final_rez = Reservierung(guest, rez.anzahl,available_room, rez.Ankunft_Zeit, rez.Abfahrt_Zeit)#Reservierung wird gemacht
        self.__lst_rez.append(final_rez)
        r.delete_room(available_room)

        self.__storeToFile()

    def filter(self, price, view):#Filtert das gewuenschte Zimmer heraus
        z = ReposRoom()
        for room in z.room_list:
            if (str(room.mon) == str(view)) and (int(room.preis) <= int(price)):#filtert nach Meeresblick(True/False) und Preis
                return room.nummer

    def available_rooms_today(self):#Sucht Zimmer die heute frei sind
        rez = Repos_gemeinsamm()
        t = ReposRoom()
        today_day = datetime.now().day
        today_month = datetime.now().month
        today_year = datetime.now().year
        list = []

        for r in (rez.return_list):
            test = r.Ankunft_Zeit
            datef = test.split('/')
            day = datef[0]
            month = datef[1]
            year = datef[2]
            if str(day) < str(today_day) and str(month) <= str(today_month) and str(year) >= str(today_year):
                list.append(r.zimmer)

        for room in t.room_list:
            if room.fon == 'True':
                list.append(room.nummer)

        return list

    @property
    def return_list(self):
        return self.__lst_rez

    def __loadFromFile(self):
        f = open(self.__fName, 'r')
        for line in f:
            data = line.strip().split(',')
            univ = Reservierung(data[0], data[1], data[2], data[3], data[4])
            self.__lst_rez.append(univ)

    def __storeToFile(self):
        f = open(self.__fName, 'w')
        for el in self.__lst_rez:
            f.write(str(el) + "\n")
        f.close()
