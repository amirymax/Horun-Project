import json

# products = [
#     {"name": "Кроссовки", "price": 10000},
#     {"name": "Куртка", "price": 12000},
#     {"name": "Рюкзак", "price": 8000}
# ]


# with open('products.json', 'w', encoding='utf-8') as file:
#     # json.dump( что сохранить, куда сохранить, indent=абзац )
#     json.dump(products, file, ensure_ascii=False, indent=2)

with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

for product in products:
    print(f'{product['name']} - {product['price']} сум')