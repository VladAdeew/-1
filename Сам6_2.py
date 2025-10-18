def tChanger(t):
    if not isinstance(t, tuple):
        return t
    tList = list(list(t)[0])
    tNumber = list(t)[1]
    for i in tList:
        if i == tNumber:
            tList.remove(i)
            break
    return tuple(tList)

t1 = ((1,2,3),1)
t2 = ((1,2,3,1,2,3,4,5,2,3,4,2,4,2),3)
t3 = ((2,4,6,6,4,2),9)
t4 = [1, 2, 3 ,4 ,5 ,6,7]

print(tChanger(t1))
print(tChanger(t2))
print(tChanger(t3))

