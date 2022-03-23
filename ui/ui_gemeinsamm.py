from tkinter import *
from tkinter import messagebox
from Repositories.Repos_rooms import ReposRoom
from Entities.Reservierung import Reservierung
from Repositories.Repos_gemeinsamm import Repos_gemeinsamm
from datetime import datetime


class Gui1:
    def __init__(self, controller, gui_master):
        self.__window = gui_master
        self.__controller = controller
        # Die Widgets für die Eingabendaten werden erstellt:
        self.__guest_name_txt = Entry(self.__window, width=50)
        self.__number_of_guests_txt = Entry(self.__window, width=50)
        self.__room_nr_txt = Entry(self.__window, width=50)
        self.__arrival_time_txt = Entry(self.__window, width=50)
        self.__check_out_time_txt = Entry(self.__window, width=50)
        self.__view_txt = Entry(self.__window, width=50)
        self.__room_price_txt = Entry(self.__window, width=50)


    def draw_window(self):
        self.__window.title("Hotel Reservation ")#Titel vom Fenster
        self.__window.geometry('650x400')#Dimension des Fensters
        # Die Knöpfe werden erstellt
        button1 = Button(self.__window, text="Make reservation", command=self.__create_list, width=13)
        button1.grid(column=2, row=0, sticky=E)
        button2 = Button(self.__window, text="Room filter", command=self.__filter_list, width=13)
        button2.grid(column=3, row=0, sticky=E)
        button3 = Button(self.__window, text="Free rooms today", command=self.__available_rooms, width=13)
        button3.grid(column=2, row=1, sticky=E)
        button4 = Button(self.__window, text="Reservations", command=self.__print_rez, width=13)
        button4.grid(column=3, row=1, sticky=E)
        # Der Text für die Art der Eingabedaten wird auf dem Fester befestigt:
        name = Label(self.__window, text='Guest name')
        name.grid(column=0, row=0, sticky=E)
        self.__guest_name_txt.grid(column=1, row=0)
        number = Label(self.__window, text='number of guests')
        number.grid(column=0,row=1,sticky=E)
        self.__number_of_guests_txt.grid(column=1, row=1)
        arrival = Label(self.__window, text='arrival time')
        arrival.grid(column=0, row=2, sticky=E)
        self.__arrival_time_txt.grid(column=1, row=2)
        ckeck_out_time = Label(self.__window, text='ckeck_out_time')
        ckeck_out_time.grid(column=0, row=3, sticky=E)
        self.__check_out_time_txt.grid(column=1, row=3)
        view = Label(self.__window, text=' See View(True/False)')
        view.grid(column=0, row=4, sticky=E)
        self.__view_txt.grid(column=1, row=4)
        price = Label(self.__window, text='Price')
        price.grid(column=0, row=5, sticky=E)
        self.__room_price_txt.grid(column=1, row=5)
        print_filter = Label(self.__window, text="Rooms with the searched criteria:")
        print_filter.grid(column=0, row=6, sticky=E)
        print_filterr = Label(self.__window, text='Free rooms:')
        print_filterr.grid(column=0, row=7, sticky=E)
        print_filterr = Label(self.__window, text='Reservations:')
        print_filterr.grid(column=0, row=8, sticky=E)
    def __create_list(self):
        rez = Reservierung(self.__guest_name_txt.get(), self.__number_of_guests_txt.get(), self.__room_nr_txt.get(),
                           self.__arrival_time_txt.get(),
                           self.__check_out_time_txt.get())  # Die Eingaben werden aufgerufen
        if self.__guest_name_txt.get() == "" or self.__number_of_guests_txt.get() == "" or self.__arrival_time_txt.get() == "" or self.__check_out_time_txt.get() == "":
            messagebox.showerror("Wrong Data", "Invalid data,Numbers only!")
            self.__guest_name_txt.delete(0, 'end')
            self.__number_of_guests_txt.delete(0, 'end')
            self.__arrival_time_txt.delete(0, 'end')
            self.__check_out_time_txt.delete(0, 'end')
            raise ValueError("Wrong data")

        if "/" in self.__arrival_time_txt.get() and "/" in self.__check_out_time_txt.get():  # ueperpruft ob die Daten im richtigen Format angebegen wurden und ob das Datum auch richtig ist
            ok = True
            day, month, year = self.__arrival_time_txt.get().split('/')
            day_out, month_out, year_out = self.__check_out_time_txt.get().split('/')

            try:
                datetime(int(year), int(month), int(day))
                datetime(int(year_out), int(month_out), int(day_out))

            except ValueError:
                ok = False
            if ok == True:
                self.__controller.add_rez(rez)  # Die Methode aus dem Controller wird aufgerufen
                # Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können:
                self.__guest_name_txt.delete(0, 'end')
                self.__number_of_guests_txt.delete(0, 'end')
                self.__arrival_time_txt.delete(0, 'end')
                self.__check_out_time_txt.delete(0, 'end')
            elif ok==False:
                self.__arrival_time_txt.delete(0, 'end')
                self.__check_out_time_txt.delete(0, 'end')
                messagebox.showerror("Wrong data", "Incorect date")
                raise ValueError("Wrong data", "Incorect date")

        else:
            self.__arrival_time_txt.delete(0, 'end')
            self.__check_out_time_txt.delete(0, 'end')
            messagebox.showerror("Wrong data", " pleasse Incorect date")



    def __filter_list(self):
        rez=Repos_gemeinsamm()
        # Die Eingaben werden aufgerufen
        price=self.__room_price_txt.get()
        view=self.__view_txt.get()

        if price.isdigit() and (view=='True' or view=='False'):
            room_lst=self.filter(price,view)##Die Methode wird aufgerufen
            text=Text(self.__window,width=20,height=1)# tkinter Widget in dem wir den Inhalt der Datei dem Nutzer zeigen werden
            text.grid(column=1,row=6)
            sep=','
            el=sep.join(room_lst)#Die Elemente der Liste werden verknüpft
            text.insert(END,el)
            self.__view_txt.delete(0, 'end')
            self.__room_price_txt.delete(0, 'end')
        else:
            messagebox.showerror("Wrong Data", "Invalid data,Numbers only!")


    def filter(self,price, view):
        z = ReposRoom()
        lst_rooms=[]
        for room in z.room_list:
            if (str(room.mon) == str(view)) and (int(room.preis) <= int(price)):
                lst_rooms.append(room.nummer)
        return lst_rooms


    def __available_rooms(self):

        free_rooms=self.available_rooms_today()

        text = Text(self.__window, width=20, height=1)
        text.grid(column=1, row=7)

        sep = ','
        el = sep.join(free_rooms)#Die Elemente der Liste werden verknüpft
        text.insert(END, el)#Ergebnis wird im Text Widget gezeigt

    def available_rooms_today(self):
        rez = Repos_gemeinsamm()
        t = ReposRoom()
        today_day = datetime.now().day
        today_month = datetime.now().month
        today_year = datetime.now().year
        list = []

        for r in (rez.return_list):
            test = r.Ankunft_Zeit
            test2=r.Abfahrt_Zeit
            datef = test.split('/')
            datef2=test2.split('/')
            day2 = datef2[0]
            month2 = datef2[1]
            year2 = datef2[2]
            day = datef[0]
            month = datef[1]
            year = datef[2]
            if int(day) > int(today_day) and int(month) >= int(today_month) and int(year) >= int(today_year) and int(day2) > int(today_day) and int(month2) >= int(today_month) and int(year2) >= int(today_year) :
                list.append(r.zimmer)
            elif int(day) > int(today_day) and int(month) >= int(today_month) and int(year) >= int(today_year) :
                list.append(r.zimmer)

        for room in t.room_list:
            if room.fon == 'True':
                list.append(room.nummer)

        return list




    def __print_rez(self):
        with open("gemeinsam", "r") as f:  # wir öffnen die Datei"gemeinsam",damit wird die Reservierungen auf dem Bildschirm anzeigen können
            content_file = Text(self.__window, width=100,height=50)  # tkinter Widget in dem wir den Inhalt der Datei dem Nutzer zeigen werden
            content_file.grid(column=1, row=9)
            lst_rooms = []
            for data_read in f:  # wir lesen die Datei(in unserem Fall werden die Reservierungen gelesen)

                data_read = data_read.strip().split('\n')

                i = 0
                rez = data_read[i].split(',')
                guest_name = rez[0]
                room_nr = rez[1]
                room_capacity = rez[2]
                check_in = rez[3]
                check_out = rez[4]
                final_format = "Guest:{}  Room capacity:{}  Room number:{}  Check in:{}  Check out:{}".format(guest_name, room_nr, room_capacity, check_in, check_out)
                # die Daten werden in einem bestimmten Format dem Nutzer gezeigt
                i += 1
                lst_rooms.append(final_format)
            for el in lst_rooms:
                content_file.insert(END, el + '\n')

        f.close()






