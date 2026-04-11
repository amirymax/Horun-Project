file = open('products.txt', 'w')
file.write('Krossovki\n')
file.write("Kurtka\n")
file.write("Ryukzak\n")
file.close()
print('Файл успешно записан')

file = open('products.txt', 'r', encoding='utf8')
content = file.read()
file.close()
print(content)

file  = open('products.txt', 'r')
for line in file:
    number = int(line.strip())
    print(number**2)

file.close()

with open('products.txt', 'a') as file:
    file.write('Krossovki\n')
    file.write("Kurtka\n")
    file.write("Ryukzak\n")




