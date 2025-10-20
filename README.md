# Адеев Владислав Николаевич АИС-23-1
# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):

- Адеев Владислав Николаевич
- АИС-23-1


| Задание  | Лаб_раб | Сам_раб |
| ------------- | ------------- | --- |
| 1 | + | + |
| 2 | + | + |
| 3 | + | + |
| 4 | + | + |
| 5 | + | + |
| 6 | + | + |
| 7 | + | + |
| 8 | + | + |
| 9 | + | + |
| 10 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### Результат
<img width="681" height="475" alt="image" src="https://github.com/user-attachments/assets/1a3a9576-c422-4edb-9c5e-a5d9a533dc96" />

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
``` Python
f = open("Lab7txt_1.txt")
print(f.readline())
f.close()
```
### Результат
<img width="1712" height="330" alt="image" src="https://github.com/user-attachments/assets/e2dd7d30-3765-43b8-b789-b606f4bf3479" />

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
``` Python
f = open("Lab7txt_1.txt")
print(f.readlines())
f.close()
```
### Результат
<img width="1706" height="326" alt="image" src="https://github.com/user-attachments/assets/be43caa2-74b5-4ed4-a5a0-446de7b67a41" />

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
``` Python
with open("Lab7txt_1.txt") as f:
    print(f.readlines())
```
### Результат
<img width="1711" height="326" alt="image" src="https://github.com/user-attachments/assets/dbf69be2-5fe6-49b6-8664-183c3b8c8773" />

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
``` Python
with open("Lab7txt_1.txt") as f:
    for line in f:
        print(line)
```
### Результат
<img width="760" height="331" alt="image" src="https://github.com/user-attachments/assets/9645d624-497c-4f79-834d-773c51305f9f" />

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
``` Python
with open("Lab7txt_1.txt", 'a+') as f:
    f.write("\nIm additional line")

with open("Lab7txt_1.txt", 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат
<img width="1153" height="301" alt="image" src="https://github.com/user-attachments/assets/0cc4adb3-286c-4e69-93c2-fb68fd130d00" />
<img width="374" height="227" alt="image" src="https://github.com/user-attachments/assets/f4947983-faff-4589-9f36-08a04d0a7128" />


## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
``` Python
lines = ['one', 'two', 'three']
with open('Lab7txt_1.txt', 'w') as f:
    for l in lines:
        f.write('\nCycle run ' + l)
    print('Done')
```
### Результат
<img width="1223" height="1080" alt="image" src="https://github.com/user-attachments/assets/5049bee0-2fed-4c5c-a38e-c67875fd414a" />

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
``` Python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит:")
    print(f'Директории: {", ".join(folder for folder in catalog[1])}')
    print(f'Файлы: {", ".join(file for file in catalog[2])}')
    print('-' * 40)


print_docs('C:/Users/User/Desktop/Java')
```
### Результат
<img width="1081" height="300" alt="image" src="https://github.com/user-attachments/assets/d5de0ec1-bc75-4ca9-b40f-cef5affa219a" />

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
``` Python
def longest_words(file):
    with open(file, encoding = 'utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('input.txt'))
```

### Результат
<img width="1080" height="297" alt="image" src="https://github.com/user-attachments/assets/052b7bda-9848-42a9-b4a6-9e3f15aeb8bc" />

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: • № - номер по порядку (от 1 до 300); • Секунда – текущая секунда на вашем ПК; • Микросекунда – текущая миллисекунда на часах. Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
``` Python
import csv
import datetime
import time
with open('rows300.csv', 'w', encoding = 'utf-8', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секуда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат
<img width="639" height="605" alt="image" src="https://github.com/user-attachments/assets/6289db41-b17a-4b86-b1c2-0d88d0a93514" />

## Самостоятельная работа №1
### 
``` Python

```
### Результат

### Вывод

## Самостоятельная работа №2
### 
``` Python

```
### Результат

### Вывод

## Самостоятельная работа №3
### 
``` Python

```
### Результат

### Вывод

## Самостоятельная работа №4
### 
``` Python

```
### Результат

## Самостоятельная работа №5
### 
``` Python

```
### Результат

### Вывод
