class Wear:
    def __init__(self, type, size):
        self._type = type
        self._size = size
        self.__inCloset = False

    def putInTheCloset(self):
        self.__inCloset = True
        print(f'Одежда {self._type}, размера {self._size} положена в шкаф')

myWear = Wear('Штаны', "M")
print(myWear._type)
print(myWear._size)
