class ContRez:
    def __init__(self, repo):
        self.__repo = repo

    def add_rez(self, rez):#Verbindung zu Repos_gemeinsamm(Methode=add_rez)
        self.__repo.add_rez(rez)


    def filter(self,price,view):#Verbindung zu Repos_gemeinsamm(Methode=filter)
        self.__repo.filter(price,view)

    def available_rooms_today(self):#Verbindung zu Repos_gemeinsamm
        self.__repo. available_rooms_today()


    def print_list(self):
        self.__repo.print_list()
