from tkinter import *
class Gui_help:
    def __init__(self,gui_master,window5,window6):
        self.__window = gui_master
        self.__window5 = window5
        self.__window6 = window6



    def draw_window(self):
        button1 = Button(self.__window, text="Help Center", command =self.__window5,width=13)
        button1.grid(column=5, row=1)
        button2 = Button(self.__window, text="Contact us",command = self.__window6, width=13)
        button2.grid(column=5, row=2)
        button1.place(relx=0.5, rely=0.5, anchor=CENTER)
        button2.place(relx=0.5, rely=0.57, anchor=CENTER)


class Gui_help2:
    def __init__(self, gui_msater,window7,window8,window9):
        self.__window = gui_msater
        self.__window7 = window7
        self.__window8 = window8
        self.__window9 = window9


    def draw_window(self):
        button1 = Button(self.__window, text="Menu Gaste Help", command=self.__window7, width=20)
        button1.grid(column=5, row=1)
        button2 = Button(self.__window, text="Menu Zimmer Help ", command=self.__window8, width=20)
        button2.grid(column=5, row=2)
        button3 = Button(self.__window, text="Menu Gemeinsamm Help", command=self.__window9, width=20)
        button3.grid(column=5, row=3)
        button1.place(relx=0.5, rely=0.5, anchor=CENTER)
        button2.place(relx=0.5, rely=0.56, anchor=CENTER)
        button3.place(relx=0.5, rely=0.62, anchor=CENTER)

class Gui_help3:
    def __init__(self, gui_msater):
        self.__window = gui_msater

    def draw_window(self):
        label1 = Label(self.__window, text='Email: hotel@gmail.com')
        label2 = Label(self.__window, text='Phone number: +40748524805')
        label3 = Label(self.__window, text='Website: https://ourwebpage.com/')
        label1.grid(column=5, row=1)
        label2.grid(column=5, row=2)
        label3.grid(column=5, row=3)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2.place(relx=0.5, rely=0.54, anchor=CENTER)
        label3.place(relx=0.5, rely=0.58, anchor=CENTER)

class Gui_help4: #fur Menu Gaste
    def __init__(self, gui_msater):
        self.__window = gui_msater

    def draw_window(self):
        label=Label(self.__window,text='- Add guest: fill in First name and Last name fields and press the button to add a new guest')
        label.grid(column=0, row=1)
        label1 = Label(self.__window, text='- Modify last name: fill in First name and Last name fields with a name that is already in the list and then fill in New last name field. After pressing the button, the name will be modified')
        label1.grid(column=0, row=2)
        label2 = Label(self.__window, text='- Delete guest: fill in First name and Last name fields with a name that is already in the list. After pressing the button, the name will be deleted.')
        label2.grid(column=0, row=3)
        label3 = Label(self.__window, text='- Show list: press the button to show the list of guests')
        label3.grid(column=0, row=4)
        label.place(relx=0, rely=0.03, anchor=W)
        label1.place(relx=0, rely=0.06, anchor=W)
        label2.place(relx=0, rely=0.09, anchor=W)
        label3.place(relx=0, rely=0.12, anchor=W)
class Gui_help5: #fur Menu Zimmer
    def __init__(self, gui_msater):
        self.__window = gui_msater

    def draw_window(self):
        label = Label(self.__window,
                      text='- Add room: fill in all the fields except the New price field and press the button to add a new room')
        label.grid(column=0, row=1)
        label1 = Label(self.__window,
                       text='- Modify price: fill in the Room number field with a number that is already in the list and the New price field. Press the button and the price of the room will be modified.')
        label1.grid(column=0, row=2)
        label2 = Label(self.__window,
                       text='- Delete room: fill in the Room number field with a number that is already in the list. Press the button and the room will be deleted.')
        label2.grid(column=0, row=3)
        label3 = Label(self.__window, text='- Show rooms: press the button to show the list of rooms.')
        label3.grid(column=0, row=4)
        label.place(relx=0, rely=0.03, anchor=W)
        label1.place(relx=0, rely=0.06, anchor=W)
        label2.place(relx=0, rely=0.09, anchor=W)
        label3.place(relx=0, rely=0.12, anchor=W)

class Gui_help6: #fur Menu Gemeinsamm
    def __init__(self, gui_msater):
        self.__window = gui_msater

    def draw_window(self):
        label = Label(self.__window,
                      text='- Make reservation: fill in the Guest name field with a name that is already in the list, the number of guests and arrival and ckeck_out time fields. Press the button and the reservation will be made.')
        label.grid(column=0, row=1)
        label1 = Label(self.__window,
                       text='- Room filter: fill in the See view with True or False in order to have See view or not. Fill in the Price field with the highest price you afford.')
        label1.grid(column=0, row=2)
        label2 = Label(self.__window,
                       text='- Free rooms today: press the button to show the rooms that are free today')
        label2.grid(column=0, row=3)
        label3 = Label(self.__window, text='- Reservations: press the button to show the list of reservations. ')
        label3.grid(column=0, row=4)
        label.place(relx=0, rely=0.03, anchor=W)
        label1.place(relx=0, rely=0.06, anchor=W)
        label2.place(relx=0, rely=0.09, anchor=W)
        label3.place(relx=0, rely=0.12, anchor=W)