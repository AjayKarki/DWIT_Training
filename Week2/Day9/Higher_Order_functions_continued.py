from functools import reduce

p1 = [1, 3]
p2 = [3, 1]
"""
Below function 1st finds the square of difference of the two points and then adds
them and finally finds the square root of sum and hence distance is calculated
"""
dist = sum(list(map(lambda x, y: (x - y) ** 2, p1, p2))) ** 0.5
print(dist)

"""
Distance from origin
"""


def distance(point):
    x, y, z = point
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5


points = [(1, 2, 3), (4, 5, 6)]
distances = list(map(distance, points))
dista = list(map(lambda p: (p[0] ** 2 + p[1] ** 2 + p[2] ** 2) ** 0.5, points))
print(distances)
print(dista)

nums = [0, 1, 2, 3, 4, 5, 9, 8, 7]
nums = list(filter(lambda x: x != 0, nums))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'o', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']
alphabets_filtered = list(filter(lambda x: x not in vowels, alphabets))
print(alphabets_filtered)


# def has_vowel(wo):
#     for w in wo:
#         if w in vowels:
#             return
#     return wo


def has_vowel(x):
    # False if set(x).intersection(set(vowels)): else True
    if set(x).intersection(set(vowels)):
        return False
    return True


list_words = ['apple', 'ball', 'tsm', 'tqm']
filtered_words = list(filter(has_vowel, list_words))
print(filtered_words)

filter_words = list(filter(lambda x: not set(x).intersection(set(vowels)), list_words))
print(filter_words)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # need to import reduce  from functools
print(product)

list_one = [1, 2, 3, 4, 5]
mean = reduce(lambda x, y: x + y, list_one) / len(list_one)
print(mean)

randomList = [1, 'a', 0, False, True, '0']
filtered_list = filter(None, randomList)
for e in filtered_list:
    print(e)
print(list(filtered_list))
