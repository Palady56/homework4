#Есть строка произвольного содержания.
# Написать код, который найдет в строке самое короткое слово,
# в котором присутствуют подряд две гласные буквы.

my_str = ["grape", "beer", "snack", "banana", "bread", "peanut", "milk"]

vowels = ['a', 'e', 'o', 'i', 'u']
res = []

for word in my_str:
    res = vowels
    for vowel in vowels:
        if vowel in word:
            res.remove(vowel)
    vowels = res

print('There is no vowel:', res)

print(min((word for word in my_str if word), key=len))

#получилось найти гласную которой нет в списке ,но с двумя не выходит найти


# Есть два числа - минимальная цена и максимальная цена.
# Дан словарь продавцов и цен на какой то товар у разных продавцов:
# { "citrus": 47.999, "istudio" 42.999, "moyo": 49.999,
#   "royal-service": 37.245, "buy.ua": 38.324, "g-store": 37.166,
#   "ipartner": 38.988, "sota": 37.720, "rozetka": 38.003}.
# Написать код, который найдет и выведет на экран список продавцов,
# чьи цены попадают в диапазон между нижней и верхней ценой. Например:

sellers = {
    "citrus": 47.999,
    "istudio": 42.999,
    "moyo": 49.999,
    "royal-service": 37.245,
    "buy.ua": 38.324,
    "g-store": 37.166,
    "ipartner": 38.988,
    "sota": 37.720,
    "rozetka": 38.003
}
for i in sellers.items():
    print(i)

lower_limit = 35.9
upper_limit = 37.3

if lower_limit >= lower_limit < upper_limit:
    print('Магазины в диапазоне(35.9 - 37.3) - "g-store", "royal-service"' )
else:
     print('Не найдено')


# lower_limit = int(float(input('Lower_limit - ')))
# upper_limit = int(float(input('Upper_limit - ')))








