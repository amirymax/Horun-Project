from functions import (show_catalog, select_product, 
                       find_product, cheapest,
                       total_price, add_product)


# Запускаем
show_catalog()

opions = '''
=== Опции ===
1. Поиск по номеру
2. Поиск по названию
3. Самый дешевый товар
4. Общая сумма
5. Добавить товар
'''

print(opions)
option = int(input("Введите номер опции: "))

if option == 1:
    number = int(input("Введи номер: "))
    select_product(number)

elif option == 2:
    name = input("Введите название товара (как в списке): ")
    print(find_product(name))

elif option == 3:
    cheapest()

elif option == 4:
    total_price()

elif option == 5:
    name = input("Введите название товара: ")
    price = int(input('Введите цену товара: '))
    add_product(name, price)
    