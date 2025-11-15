def checkDigit(func):  #Декоратор, который принимает функцию
    def wrapper(*args): #Функция, которая расширяет другую функцию
        num = args[0] #Присваиваем значение
        if num >= 10: #Условие
            num = 40+num
        elif num < 10:
            num = 10*num
        func(num) #Передаем значение в функцию
    return wrapper

@checkDigit
def summator(num):
    print(num)

summator(11)
