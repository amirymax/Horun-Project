from functions import (show_catalog, select_product,
                       find_product, cheapest,
                       total_price, add_product,
                       delete_product, add_to_cart, 
                       show_cart, remove_from_cart,
                       clear_cart, count_cart,
                       most_expensive, load_products,
                       save_products, edit_price)

from time import sleep

load_products()

show_catalog()

options = '''
=== Опции ===
1. Поиск по номеру
2. Поиск по названию
3. Самый дешевый товар
4. Общая сумма
5. Добавить товар
6. Удалить товар
7. Добавить в корзину
8. Показать корзину
9. Удалить из корзины
10. Очистить корзину
11. Количество товаров в корзине
12. Самый дорогой товар в магазине
13. Изменить цену
'''

while True:
    print(options)
    option = int(input("Введите номер опции: "))

    if option == 1:
        number = int(input("Введи номер: "))
        select_product(number)
    elif option == 2:
        name = input("Введите название товара: ")
        print(find_product(name))
    elif option == 3:
        cheapest()
    elif option == 4:
        total_price()

    elif option == 5:
        name = input("Введите название товара: ")
        price = int(input("Введите цену: "))
        add_product(name, price)
        save_products()

    elif option == 6:
        show_catalog()
        number = int(input("Введи номер товара для удаления: "))
        delete_product(number)
        save_products()


    elif option == 7:
        show_catalog()
        number = int(input("Введи номер товара: "))
        add_to_cart(number)

    elif option == 8:
        show_cart()
    
    elif option == 9:
        cart = show_cart()
        if cart == 1:
            number = int(input("Введи номер товара в корзине: "))
            remove_from_cart(number)
        # else:
        #     sleep(3)
        #     continue
    elif option == 10:
        clear_cart()
        print('Корзина была очищена')
    
    elif option == 11:
        print(f'В корзине {count_cart()} товаров')
    
    elif option == 12:
        most_expensive()
    
    elif option == 13:
        show_catalog()
        number = int(input("Введите номер товара: "))
        new_price = int(input("Введите новую цену: "))

        edit_price(number, new_price)
        save_products()
    
    sleep(3)
