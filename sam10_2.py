def summator(digit):
    try:
        result = digit+2
        print(result)
    except TypeError:
        print("Неподходящий тип данных. Ожидалось число.")

summator('asd')
