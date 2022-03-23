class Conoller:
    def __init__(self, repo):
        self.__repo = repo

    def add_room(self, room):#Verbindung zu Repos_rooms(Methode=add)
        self.__repo.add(room)

    def modify_price(self, room, new_prce):#Verbindung zu Repos_rooms(Methode=modify)
        self.__repo.modify_price(room, new_prce)

    def delete_room(self, room_nr):#Verbindung zu Repos_rooms(Methode=delete)
        self.__repo.delete_room(room_nr)

    def print_list(self):#Verbindung zu Repos_rooms
        self.__repo.print_list()
