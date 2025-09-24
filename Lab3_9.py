even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True


if flag == True:
    print("В массиве есть нечетные числа")
else:
    print('В массиве все числа четные')