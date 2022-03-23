from Controller.Controller_Gast import Cont
from Repositories.Repository_Gast import Repository_Gast
from Controller.Contoller_rooms import Conoller
from Repositories.Repos_rooms import ReposRoom
from Repositories.Repos_gemeinsamm import Repos_gemeinsamm
from Controller.Controller_rez import ContRez
from tkinter import *
from ui.ui import Gui
from ui.ui_room import GUI
from ui.ui_gemeinsamm import Gui1
from ui.ui_help import Gui_help
from ui.ui_help import Gui_help2
from ui.ui_help import Gui_help3
from ui.ui_help import Gui_help4
from ui.ui_help import Gui_help5
from ui.ui_help import Gui_help6


def main():
    window = Tk()
    window.title("menu")
    window.geometry("400x300")

    def new_window1():#Fenster fuer Gast Menu wird erstellt
        new_window1 = Tk()
        new_window1.title("Gast")
        new_window1.geometry("300x300")
        repo = Repository_Gast()
        control = Cont(repo)
        g = Gui(control, new_window1)
        g.draw_window()

    def new_window2():#Fenster fuer Zimmer Menu wird erstellt
        new_window2 = Tk()
        new_window2.title("Zimmer")
        new_window2.geometry("300x300")
        reporoom = ReposRoom()
        controlRoom = Conoller(reporoom)
        r = GUI(controlRoom, new_window2)
        r.draw_window()

    def new_window3():#Fenster fuer Gemeinsamm Menu wird erstellt
        new_window3 = Tk()
        new_window3.title("Gemeinsamm")
        new_window3.geometry("500x500")
        repogemeinsamm = Repos_gemeinsamm()
        controlRez = ContRez(repogemeinsamm)
        z = Gui1(controlRez, new_window3)
        z.draw_window()

    def new_window4():
        new_window4 = Tk()
        new_window4.title("Help")
        new_window4.geometry("500x500")
        ama = Gui_help(new_window4, new_window5, new_window6)
        ama.draw_window()


    def new_window5():
        new_window5 = Tk()
        new_window5.title("Help Center")
        new_window5.geometry("500x500")
        ama2 = Gui_help2(new_window5, new_window7, new_window8, new_window9)
        ama2.draw_window()

    def new_window6():
        new_window6 = Tk()
        new_window6.title("Contact us")
        new_window6.geometry("500x500")
        ama3 = Gui_help3(new_window6)
        ama3.draw_window()

    def new_window7():
        new_window7 = Tk()
        new_window7.title("Menu Gast")
        new_window7.geometry("500x500")
        ama4 = Gui_help4(new_window7)
        ama4.draw_window()

    def new_window8():
        new_window8 = Tk()
        new_window8.title("Menu Zimmer")
        new_window8.geometry("500x500")
        ama5 = Gui_help5(new_window8)
        ama5.draw_window()

    def new_window9():
        new_window9 = Tk()
        new_window9.title("Menu Gemeinsamm")
        new_window9.geometry("500x500")
        ama6 = Gui_help6(new_window9)
        ama6.draw_window()

    # Die Knöpfe werden erstellt
    button = Button(window, text='Help', command=new_window4, width=15)
    button.grid(row=1, column=0)
    button1 = Button(window, text="Menu Gast", command=new_window1, width=15)
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    container = Frame(window)
    container.grid(row=0, column=0)
    button1.grid(pady=10, padx=20)
    button2 = Button(window, text="Menu Zimmer", command=new_window2, width=15)
    button2.grid(pady=(0, 10), padx=20, sticky=N)
    button3 = Button(window, text="Menu Gemeinsam", command=new_window3, width=15)
    button3.grid(pady=(0, 10), padx=20, sticky=N)
    button4=Button(window,text="Quit",command=window.destroy,width=15)
    button4.grid(pady=(0, 10), padx=20, sticky=N)
    window.mainloop()


main()
