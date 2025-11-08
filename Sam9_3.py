class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state == 3:
            pass
        else:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

class TomatoBush:
    def __init__(self, num):
        self.tomato = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomato:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomato)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        if self._plant.tomato:
            self._plant.grow_all()
            print("Садовник полил помидорки")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"Садовник {self.name} собрал урожай!")
        else:
            print(f"Не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1). Вовремя поливайте")
        print("2). Не дайте перезреть помидоркам(вовремя собирайте)")
        print("3). Относитесь бережно")

bush = TomatoBush(4)
gardener = Gardener("Николай", bush)

gardener.harvest()