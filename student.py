# Student Class

class Student:

    # Initialize student attributes
    def __init__(self, id, first_name, last_name, age, song_1, song_2, song_3, teacher_name, performance_time):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__song_1 = song_1
        self.__song_2 = song_2
        self.__song_3 = song_3
        self.__teacher_name = teacher_name
        self.__performance_time = performance_time

    # Mutator methods
    def set_id(self, id):
        self.__id = id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age

    def set_song_1(self, song_1):
        self.__song_1 = song_1

    def set_song_2(self, song_2):
        self.__song_2 = song_2

    def set_song_3(self, song_3):
        self.__song_3 = song_3

    def set_teacher_name(self, teacher_name):
        self.__teacher_name = teacher_name

    def set_performance_time(self, performance_time):
        self.__performance_time = performance_time

    # Accessor methods
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_song_1(self):
        return self.__song_1

    def get_song_2(self):
        return self.__song_2

    def get_song_3(self):
        return self.__song_3

    def get_teacher_name(self):
        return self.__teacher_name

    def get_performance_time(self):
        return self.__performance_time
