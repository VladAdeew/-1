def longestNumber(numbers):
    if len(numbers) < 15:
        return print("Длина числа менее 15")


    dictNumbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    numbers = int(numbers)

    for i in range(len(str(numbers))):
        digit = numbers % 10
        if digit == 0:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 1:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 2:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 3:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 4:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 5:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 6:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 7:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 8:
            dictNumbers[digit] = dictNumbers[digit] + 1
        elif digit == 9:
            dictNumbers[digit] = dictNumbers[digit] + 1
        numbers = numbers // 10

    sortedDictNumbers = sorted(dictNumbers.items(), key=lambda x: x[1], reverse=True)

    return sortedDictNumbers[:3]




numbersInput = int(input())
numbersInput = str(numbersInput)
print(longestNumber(numbersInput))