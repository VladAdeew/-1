# Адеев Владислав Николаевич АИС-23-1
# Тема 9. Концепции и принципы ООП.
Отчет по Теме #9 выполнил(а):

- Адеев Владислав Николаевич
- АИС-23-1


| Задание  | Лаб_раб | Сам_раб |
| ------------- | ------------- | --- |
| 1 | + | + |
| 2 | + | + |
| 3 | + | + |
| 4 | + | + |
| 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.
``` Python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f'Да, я {name}'
        else:
            self.name = f'Нет, я не {name}, меня зовут Иван'

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)     

person2.surname = "Петров"
```
### Результат
<img width="1703" height="378" alt="image" src="https://github.com/user-attachments/assets/24242caf-68d4-40bf-bcab-63d1ebbe225e" />

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.
``` Python
class Icecream:
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print("Обычное мороженное")

icecream = Icecream()
icecream.composition()
icecream = Icecream("Шоколадом")
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат
<img width="1709" height="293" alt="image" src="https://github.com/user-attachments/assets/f3c030c2-1bda-4764-9c22-a85352be385d" />

## Лабораторная работа №3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.
``` Python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value
    def get_value(self):
        return self._value
    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойства value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат
<img width="1709" height="296" alt="image" src="https://github.com/user-attachments/assets/82140207-e58f-4247-9395-83298b7f0eb0" />

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.
``` Python
class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = "canine"
    sound = "wow"

class Cat(Mammal):
    species = "feline"
    sound = "meow"

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sound}.")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sound}.")
```
### Результат
<img width="1710" height="297" alt="image" src="https://github.com/user-attachments/assets/82961c8d-c32d-4f9d-a1e1-b731086edc7f" />

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.
``` Python
class English:
    @staticmethod
    def greeting():
        print("Hello")

class Russia:
    @staticmethod
    def greeting():
        print("Привет")

def greet(language):
    language.greeting()

Ivan = Russia()
John = English()
greet(Ivan)
greet(John)
```
### Результат
<img width="1718" height="299" alt="image" src="https://github.com/user-attachments/assets/f793faad-a5b7-40aa-b6bc-f2365352f958" />

## Самостоятельная работа №1
### Вызовите справку по садоводству
``` Python
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
        for i in range(num):
            self.tomato = Tomato(i)

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

Gardener.knowledge_base()
```
### Результат
<img width="1709" height="301" alt="image" src="https://github.com/user-attachments/assets/4577c746-9b8b-498b-b7e4-3238c3718f3e" />

### Вывод
Я разобрался с работой staticmethod

## Самостоятельная работа №2
### Создайте объекты классов TomatoBush и Gardener
``` Python
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
        for i in range(num):
            self.tomato = Tomato(i)

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
print(gardener.name)
```
### Результат
<img width="1702" height="296" alt="image" src="https://github.com/user-attachments/assets/b1918f61-21ec-422f-b909-6b6dc27706f8" />

### Вывод
Я научился присваивать и вызывать данные объекту в классе

## Самостоятельная работа №3
### Используя объект класса Gardener, поухаживайте за кустом с помидорами
``` Python
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

for i in range(2):
    gardener.work()
```
### Результат
<img width="1708" height="297" alt="image" src="https://github.com/user-attachments/assets/9fd80993-9552-4b04-bb35-55b23ae38070" />

### Вывод
Я научился пользоваться методами класса

## Самостоятельная работа №4
### Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними
``` Python
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
```
### Результат
<img width="1712" height="294" alt="image" src="https://github.com/user-attachments/assets/82c6f62c-5c8b-43a6-bd86-2c0fe2a30aa5" />

### Вывод
Я научился пользоваться методами класса

## Самостоятельная работа №5
### Соберите урожай
``` Python
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

while not bush.all_are_ripe():
    gardener.work()
    gardener.harvest()

gardener.harvest()
```
### Результат
<img width="1708" height="441" alt="image" src="https://github.com/user-attachments/assets/aa3fa933-8dc2-4134-9dea-cba8cebc67bc" />

### Вывод
Я научился применять на практике принципы и концепции объектно-ориентированного программирования
