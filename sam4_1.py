import random

def Cube(rand):
    print(rand)
    if rand == 3 or rand == 4:
        Cube(random.randint(1, 6))
    elif rand == 1 or rand == 2:
        print("Вы проиграли")
    elif rand == 5 or rand == 6:
        print("Вы победили!")

if __name__ == '__main__':
    Cube(random.randint(1,6))