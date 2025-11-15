class Negative(Exception): #Создаем собственное исключение
    pass


def checkFigure(num):
    try: # Проверяем тип int
        if num >= 10:
            raise Negative(f"{num} - это число, а не цифра") #Возвращаем исключение при вводе числа, а не цифра
        else:
            print(f"{num} - это цифра!!")
    except TypeError: #Возвращаем исключение при типе отличном от int
        print("Ожидается тип int!")

checkFigure(10)

