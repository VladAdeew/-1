def mnojestvo(list1):
    list1.sort()
    list2 = [list1[0]]
    cnt = 0
    for j in range(1, len(list1)):
        if list1[j] == list1[j-1]:
            list2.append(str(list2[cnt]) + str(list1[j]))
            cnt += 1
        else:
            list2.append(list1[j])
            cnt += 1
    return list2


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(mnojestvo(list_1))
print(mnojestvo(list_2))
print(mnojestvo(list_3))