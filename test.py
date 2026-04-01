#  площадь прямоугольника

#  s = a * b

# _________a________ a=5
# |                |
# |                |b=4
# |________________|

#  5*4 = 20

# def rect(a, b): # rectangle - прямоугольник
#     # print(a*b)
#     # return - возврашать

#     return a * b 
# # Длина, Ширина
# a1, b1 = 5, 4
# a2, b2 = 10, 20
# a3, b3 = 7, 8

# rect(a1, b1)

# s1 = rect(a1, b1)
# s2 = rect(a2, b2)
# s3 = rect(a3, b3)

# #  None - нет, нет ответа
# print(f"S1 = {s1}")
# print(f"S2 = {s2}")
# print(f"S3 = {s3}")

numbers = [321,543,756,987,546,234]

def find(num):
    for i in numbers:
        if i == num:
            return "Да"
    return "Нет"

n = int(input())

for i in range(1, 1000):
    print(f'{i} найден')
    if i == n:
        break # - сломать


# num = int(input())
# print(find(num))