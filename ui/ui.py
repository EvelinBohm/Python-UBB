from tkinter import *
from Entities.Gast import Gast


class Gui:
    def __init__(self, controller, gui_master):
        self.__window = gui_master
        self.__controller = controller
        # Die Widgets für die Eingabendaten werden erstellt:
        self.__guest_first_name_txt = Entry(self.__window, width=50)
        self.__guest_last_name_txt = Entry(self.__window, width=50)
        self.__guest_new_last_name_txt = Entry(self.__window, width=50)

    def draw_window(self):
        self.__window.title("Hotel Reservation App")#Titel vom Fenster
        self.__window.geometry('650x200')#Dimension des Fensters
        # Die Knöpfe werden erstellt
        button1 = Button(self.__window, text="Add guest", command=self.__create_list,width=13)
        button1.grid(column=2, row=0, sticky=E)
        button2 = Button(self.__window, text="modify last name", command=self.__update_list,width=13)
        button2.grid(column=3, row=0, sticky=W)
        button3 = Button(self.__window, text="Delete guest", command=self.__delete_guest,width=13)
        button3.grid(column=3, row=1, sticky=W)
        button4 = Button(self.__window, text="Show list", command=self.__print_list,width=13)
        button4.grid(column=2, row=1, sticky=E)
        # Der Text für die Art der Eingabedaten wird auf dem Fester befestigt:
        first_name = Label(self.__window, text='First name')
        first_name.grid(column=0, row=0, sticky=E)
        self.__guest_first_name_txt.grid(column=1, row=0)
        last_name = Label(self.__window, text='Last name')
        last_name.grid(column=0, row=1, sticky=E)
        self.__guest_last_name_txt.grid(column=1, row=1)
        new_last_name = Label(self.__window, text='New last name')
        new_last_name.grid(column=0, row=2, sticky=E)
        self.__guest_new_last_name_txt.grid(column=1, row=2)
        print_guests = Label(self.__window, text='List of guests')
        print_guests.grid(column=0, row=3, sticky=E)

    def __create_list(self):
        guest = Gast(self.__guest_first_name_txt.get(), self.__guest_last_name_txt.get())#Die Eingaben werden aufgerufen
        self.__controller.add(guest)#Die Methode add aus dem Controller wird aufgerufen
        # Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können:
        self.__guest_first_name_txt.delete(0, 'end')
        self.__guest_last_name_txt.delete(0, 'end')

    def __update_list(self):
        guest = Gast(self.__guest_first_name_txt.get(), self.__guest_last_name_txt.get())#Die Eingaben werden aufgerufen
        new_last = self.__guest_new_last_name_txt
        self.__controller.modify(guest, new_last.get())#Die Methode modify aus dem Controller wird aufgerufen
        # Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können:
        self.__guest_first_name_txt.delete(0, 'end')
        self.__guest_last_name_txt.delete(0, 'end')
        self.__guest_new_last_name_txt.delete(0, 'end')

    def __delete_guest(self):
        guest = Gast(self.__guest_first_name_txt.get(), self.__guest_last_name_txt.get())#Die Eingaben werden aufgerufen
        self.__controller.delete(guest)#Die Methode delete wird aus dem Controller wird aufgerufen
        # Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können:
        self.__guest_first_name_txt.delete(0, 'end')
        self.__guest_last_name_txt.delete(0, 'end')


    def __print_list(self):

        with open("data", "r") as f:# wir öffnen die Datei"data",damit wird die Namen der Geste auf dem Bildschirm anzeigen können
            content_file=Text(self.__window,width=40)#Text Widget wird auf den Bildschirm plaziert
            content_file.grid(column=1, row=4, sticky=E)
            data_read=f.read()# wir lesen die Datei(in unserem Fall werden die Namen der Gaste gelesen)
            content_file.delete('1.0',END)
            content_file.insert(END,data_read)

        f.close()#die Datei wird geschlossen


