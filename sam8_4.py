class Wear:
    def HumanOrDog(self):
        pass

class HumanWear(Wear):
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def HumanOrDog(self):
        print('Человеческая одежда, т. к. нет ошейника')

class DogWear(Wear):
    def __init__(self, type, size, collar):
        self.type = type
        self.size = size
        self.collar = collar

    def HumanOrDog(self):
        print("Собачья одежда, т. к. с ошейником")

AllWear = [HumanWear('Штаны', 'M'), DogWear('Куртка', 'S', 'Зеленый')]
for wear in AllWear:
    wear.HumanOrDog()