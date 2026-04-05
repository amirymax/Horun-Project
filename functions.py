products = [
    {'name': 'Кроссовки', 'price': 10000},
    {'name': 'Куртка', 'price': 12000},
    {'name': 'Рюкзак', 'price': 8000}
]

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
