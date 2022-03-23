class Cont:
    def __init__(self, repo):
        self.__repo = repo

    def add(self, name):#Verbindung zu Repository(Methode=add)
        self.__repo.add(name)

    def modify(self, name, new_last):#Verbindung zu Repository(Methode=modify)
        self.__repo.modify(name, new_last)

    def delete(self, name):#Verbindung zu Repository(Methode=delete)
        self.__repo.delete(name)

    def print_list(self):#Verbindung zu Repository
        self.__repo.print_list()
