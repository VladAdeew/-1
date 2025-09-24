number = int(input())
if number <= 10 and number >= 0:
    if number >= 0 and number <= 3:
        print(number, "больше либо равен 0, но меньше либо равен 3")
    if number >= 4 and number < 6:
        print(number, "больше либо равен 4, но меньше 6")
    if number >= 6 and number <= 10:
        print(number, "больше либо равен 6, но меньше либо равен 10")
else:
    print("Неверное значение, введите заного значение от 0 до 10")