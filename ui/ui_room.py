from tkinter import *
from Entities.Zimmer import Zimmer
#from Repos_rooms.Repos_rooms import ReposRoom
import webbrowser
from tkinter import messagebox



class GUI:
    def __init__(self, controller, gui_master):
        self.__window = gui_master
        self.__controller = controller
        #Die Widgets für die Eingabendaten werden erstellt:
        self.__room_number_txt = Entry(self.__window, width=20)
        self.__room_capacity_txt = Entry(self.__window, width=20)
        self.__room_price_txt = Entry(self.__window, width=20)
        self.__room_color_txt = Entry(self.__window, width=20)
        self.__room_booking_status_txt = Entry(self.__window, width=20)
        self.__room_view_txt = Entry(self.__window, width=20)
        self.__room_new_price_txt = Entry(self.__window, width=20)


    def draw_window(self):
        self.__window.title("Hotel Reservation App")
        self.__window.geometry('650x400')
        button1 = Button(self.__window, text="Add room", command=self.__create_list, width=13)#Die Knöpfe werden erstellt
        button1.grid(column=0, row=7, sticky=E,padx=10,pady=1)
        button2 = Button(self.__window, text="modify price", command=self.__modify_list,width=13)
        button2.grid(column=1, row=7, sticky=W+E)
        button3 = Button(self.__window, text="Delete room", command=self.__delete_room, width=13)
        button3.grid(column=0, row=8, sticky=W,padx=10)
        button4 = Button(self.__window, text="Show rooms", command=self.__print_list, width=13)
        button4.grid(column=1, row=8, sticky=W+E)
        # Der Text für die Art der Eingabedaten wird auf dem Fester befestigt:
        room_number = Label(self.__window, text='Room number:')
        room_number.grid(column=0, row=0, sticky=E)
        self.__room_number_txt.grid(column=1, row=0)
        room_capacity = Label(self.__window, text='Room capacity:')
        room_capacity.grid(column=0, row=1, sticky=E)
        self.__room_capacity_txt.grid(column=1, row=1)
        room_price = Label(self.__window, text='Room price:')
        room_price.grid(column=0, row=2, sticky=E)
        self.__room_price_txt.grid(column=1, row=2)
        room_color = Label(self.__window, text='Room color:')
        room_color.grid(column=0, row=3, sticky=E)
        self.__room_color_txt.grid(column=1, row=3)
        room_booking_status = Label(self.__window, text='Availability:')
        room_booking_status.grid(column=0, row=4, sticky=E)
        self.__room_booking_status_txt.grid(column=1, row=4)
        room_view = Label(self.__window, text='Room view')
        room_view.grid(column=0, row=5, sticky=E)
        self.__room_view_txt.grid(column=1, row=5)
        room_new_price = Label(self.__window, text='New price')
        room_new_price.grid(column=0, row=6, sticky=E)
        self.__room_new_price_txt.grid(column=1, row=6)
        show_rooms = Label(self.__window, text='Room list:',)
        show_rooms.grid(column=0, row=9, sticky=W)
        show_rooms.config(font=("Courier",10))


    def __create_list(self):
        guest = Zimmer(self.__room_number_txt.get(), self.__room_capacity_txt.get(), self.__room_price_txt.get(),
                       self.__room_color_txt.get(), self.__room_booking_status_txt.get(), self.__room_view_txt.get())#Die Eingaben werden aufgerufen
        nr = self.__room_number_txt.get()
        cap = self.__room_capacity_txt.get()
        price = self.__room_price_txt.get()
        col = self.__room_color_txt.get()
        status = self.__room_booking_status_txt.get()
        view = self.__room_view_txt.get()
        test_color=type(col)
        if nr.isdigit() and cap.isdigit() and price.isdigit() and test_color==str and (status=='True' or status=='False') and (view=='True' or view=='False'):
            self.__controller.add_room(guest)#Die Methode aus dem Controller wird aufgerufen
            self.__room_number_txt.delete(0, 'end')#Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können
            self.__room_capacity_txt.delete(0, 'end')
            self.__room_price_txt.delete(0, 'end')
            self.__room_color_txt.delete(0, 'end')
            self.__room_booking_status_txt.delete(0, 'end')
            self.__room_view_txt.delete(0, 'end')
        else:
            self.__room_number_txt.delete(0,'end')  # Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können
            self.__room_capacity_txt.delete(0, 'end')
            self.__room_price_txt.delete(0, 'end')
            self.__room_color_txt.delete(0, 'end')
            self.__room_booking_status_txt.delete(0, 'end')
            self.__room_view_txt.delete(0, 'end')
            messagebox.showerror("Wrong Data","Invalid data!")


    def __modify_list(self):
        new_price = self.__room_new_price_txt.get()
        nr = self.__room_number_txt.get()
        if new_price.isdigit() and nr.isdigit():
            self.__controller.modify_price(nr, new_price)#Die Methode aus dem Controller wird aufgerufen
            self.__room_new_price_txt.delete(0, 'end')#Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können
            self.__room_number_txt.delete(0, 'end')
        else:
            messagebox.showerror("Wrong Data", "Invalid data,Numbers only!")
            self.__room_new_price_txt.delete(0, 'end')#Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können
            self.__room_number_txt.delete(0, 'end')

    def __delete_room(self):
        room_number = self.__room_number_txt.get()
        if room_number.isdigit():
            self.__controller.delete_room(room_number)#Die Methode aus dem Controller wird aufgerufen
            self.__room_number_txt.delete(0, 'end')#Der Inhalt der Eingabezeilen wird gelöst,damit erneut Eingaben eingegeben werden können
        else:
            messagebox.showerror("Wrong Data", "Invalid data,Numbers only!")
            self.__room_number_txt.delete(0, 'end')



    def __print_list(self):

        with open("rooms", "r") as f:# wir öffnen die Datei"rooms",damit wird die Zimmer auf dem Bildschirm anzeigen können
            content_file = Text(self.__window,width=150)# tkinter Widget in dem wir den Inhalt der Datei dem Nutzer zeigen werden
            content_file.grid(column=3, row=10)
            lst_rooms=[]
            for data_read in f:#wir lesen die Datei(in unserem Fall werden die Zimmer gelsen)

                data_read=data_read.strip().split('\n')

                i=0
                room=data_read[i].split(' ')
                room_nr=room[0]
                room_capacity=room[1]
                room_price=room[2]
                room_color=room[3]
                room_availability=room[4]
                room_view=room[5]
                final_format="Room number:{}  Room capacity:{}  Room price:{}  Room color:{}  Room availability:{}  Room view:{}".format(room_nr,room_capacity,room_price,room_color,room_availability,room_view)
                #die Daten werden in einem bestimmten Format dem Nutzer gezeigt
                i += 1
                lst_rooms.append(final_format)
            for el in lst_rooms:
                content_file.insert(END,el+'\n')


        f.close()



