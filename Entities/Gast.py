class Gast:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__lst_resgast=[]

    def __str__(self):
        return "{} {}".format(self.__first_name, self.last_name)
    def __eq__(self, other):
        return self.__first_name==other.__first_name and self.__last_name==other.__last_name
        #and self.__lst_resgast==other.__lst_resgast

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name




