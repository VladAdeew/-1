class Wear:
    def __init__(self, type, size):
        self.type = type
        self.size = size
        self.inCloset = False

    def putInTheCloset(self):
        self.inCloset = True
        print(f'Одежда {self.type}, размера {self.size} положена в шкаф')

class petWear(Wear):
    def __init__(self, type, size, collar):
        super().__init__(type, size)
        self.collar = collar
        self.CollarOn = False

    def putOnACollar(self):
        self.CollarOn = True
        print(f"{self.collar} ошейник надет")



petWear = petWear('Куртка', "S", "Зеленый")
petWear.putInTheCloset()
petWear.putOnACollar()

