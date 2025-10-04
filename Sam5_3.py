def del2(a):
    b = []
    for x in a:
        if x == 3:
            b.append(4)
        if x >= 4:
            b.append(x)
    return b

a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(del2(a))
print(del2(b))
print(del2(c))
