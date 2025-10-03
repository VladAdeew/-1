global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Длина: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    b = float(input("Высота: "))
    global result
    result = a * b * 0.5

figure = input("1 - прямоугольник, 2 - треугольник: ")

if figure == "1":
    rectangle()
elif figure == "2":
    triangle()

print(f"Площадь: {result}")