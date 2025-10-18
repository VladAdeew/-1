def searchDigit(tuple, digit, cnt):
    cntDef = 0
    for item in tuple:
        if item == digit:
            cntDef += 1
            if cntDef == cnt:
                return print("Да")

    return print("Число есть, но встречается меньше раз, чем требуется") if cntDef < cnt and cntDef != 0 else print("Число отсутствует")

enter = input("Введите кортеж: ")
enter = tuple(int(item) for item in enter.split())
digit = int(input("Искомое число: "))
cnt = int(input("Введите количество искомого числа: "))
searchDigit(enter, digit, cnt)