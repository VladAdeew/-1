from math import sqrt
def S(a, b, c):
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    return s

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max1 = max(one)
min1 = min(one)
max2 = max(two)
min2 = min(two)
max3 = max(three)
min3 = min(three)

print(S(max1, max2, max3), "- максимальная площадь")
print(S(min1, min2, min3), "- минимальная площадь")