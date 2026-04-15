import json
products = []

def show_catalog(): # показвать каталог
    print("=== Магазин ===")
    for i in range(len(products)):
        product = products[i]
        print(f"{i + 1}. {product['name']} — {product['price']} сум ({discount(product['price'], 10)} со скидкой 10% для пенсионеров)")

def select_product(number): # выбрать товар
    if number < 1 or number > len(products):
        print("Такого товара нет!")
    else:
        product = products[number - 1]
        print(f"Ты выбрал: {product['name']}")
        print(f"Цена: {product['price']} сум")


# Функция поиска товара по названию
def find_product(name):
    for i in products:
        if i == name:
            return "Есть такой товар"
    else:
        return "Нет такого товара"

# Функция показать самый дешёвый товар
def cheapest():
    product = min(products, key=lambda p: p["price"])
    print(f"Самый дешевый: {product['name']} — {product['price']} сум")

# # Функция показать общую сумму всех товаров
def total_price():
    # s = 0
    # for product in products:
    #     s += product['price']
        
    total = sum(product['price'] for product in products)

    print(f"Общая сумма всех товаров: {total} сум")


def discount(price, percent):
    return price - (price * percent/100) # 10000 - 10%

def add_product(name, price):

    # {'name': 'Рюкзак', 'price': 8000}
    product = {'name': name, 'price': price}
    products.append(product)
    print(f"Товар '{name}' добавлен!")
    show_catalog()

def delete_product(number):
    if number < 1 or number > len(products):
        print('Такого товара нет')
    else:
        product = products.pop(number-1)
        print(f'Товар {product['name']} удалён')
        show_catalog()

cart = []

def add_to_cart(number):
    if number < 1 or number > len(products):
        print('Такого товара нет')
    
    else:
        product = products[number - 1]
        cart.append(product)
        print(f"'{product['name']}' добавлен в корзину")

def show_cart():
    if len(cart) == 0:
        print('Корзина пуста!')
        return 0
    else:
        print("=== Корзина ===")
        total = 0
        for i in range(len(cart)):
            product = cart[i]
            print(f"{i + 1}. {product['name']} - {product['price']} сум")
            total += product['price']
        print(f'Итого {total} сум')
        return 1
    

def remove_from_cart(number):
    if len(cart) == 0:
        print('Корзина пуста!')
    
    elif number < 1 or number > len(products):
        print('Такого товара нет')
    
    else:
        product = cart.pop(number - 1)
        print(f"'{product['name']}' удалён из корзины!")
        show_cart()

# ДЗ

def clear_cart():
    #  очистить корзину
    cart.clear()

def count_cart():
    # количество товаров в корзине
    return len(cart)

def most_expensive():
    # самый дорогой товар в магазине
    product = max(products, key=lambda p: p["price"])
    print(f"Самый дорогой товар: {product['name']} — {product['price']} сум")


# Сохранить товары в файл
def save_products():
    with open("products.json", "w", encoding='utf8') as file:
        json.dump(products, file, ensure_ascii=False, indent=2)
    print("Товары сохранены!")

# Загрузить товары из файла
def load_products():
    global products
    try:
        with open("products.json", "r", encoding='utf8') as file:
            products = json.load(file)

        print("Товары загружены!")
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка")


def edit_price(number, new_price):
    products[number-1]['price'] = new_price
    print(f'Цена товара {products[number-1]['name']} изменена на {new_price}')
