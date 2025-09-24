values = [0, 2, 4, 6, 8, 10]
string = 'hello'
memory = ' world'
print(string + memory)
memory = string
string = string + ' world'
counter = 0
while counter != 10:
    if counter in values:
        print(memory)
        print(string)
    counter += 1
