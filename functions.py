products = ["Кроссовки", "Куртка", "Рюкзак"] # товары
prices = [10000, 12000, 8000] # цена

def show_catalog(): # показвать каталог
    print("=== Магазин ===")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]} — {prices[i]} сум")

def select_product(number): # выбрать товар
    if number < 1 or number > len(products):
        print("Такого товара нет!")
    else:
        print(f"Ты выбрал: {products[number - 1]}")
        print(f"Цена: {prices[number - 1]} сум")


# Функция поиска товара по названию
def find_product(name):
    for i in products:
        if i == name:
            return "Есть такой товар"
    else:
        return "Нет такого товара"

# Функция показать самый дешёвый товар
def cheapest():
    minimum_price = min(prices)
    index = prices.index(minimum_price)
    minimum_product = products[index]
    print(f'Самый дешевый товар это {minimum_product} по цене {minimum_price}сум')

# # Функция показать общую сумму всех товаров
def total_price():
    print(f"Общая сумма всех товаров: {sum(prices)} сум")



# ### 3. ДЗ — 5 мин
# Добавить в магазин функцию `discount(number, percent)` — принимает номер товара и процент скидки, выводит новую цену:
# ```
# Товар: Куртка
# Скидка: 10%
# Новая цена: 10800 сум