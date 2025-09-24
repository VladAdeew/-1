text = input()
print(len(text))
print(text.lower())
cnt = 0
for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)
print(text.replace('ugly', 'beauty', 1))
if text[0] == 'T' and text[1] == 'h' and text[2] == 'e' and text[-1] == 'd' and text[-2] == 'n' and text[-3] == 'e':
    print("Начинается с The, заканчивается end")
else:
    print("Не начинается с The и не заканчивается end")