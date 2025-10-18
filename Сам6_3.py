def FirstInFirstOut(tuple, id):
    FirstIn = 0
    FirstOut = 0
    voidTuple = ()
    cnt = 0
    for i in range(len(tuple)):
        if tuple[i] == id and cnt == 1:
            FirstOut = i+1
            return tuple[FirstIn:FirstOut]
        if tuple[i] == id and cnt == 0:
            cnt += 1
            FirstIn = i
    return tuple[FirstIn::] if FirstIn != 0 else voidTuple

enter = input("Введите порядок входа/выхода: ")
idIn = int(input("Введите id: "))
enter = tuple(int(item) for item in enter.split())
print(FirstInFirstOut(enter, idIn))
