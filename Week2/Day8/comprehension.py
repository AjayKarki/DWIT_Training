list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [num for num in list1 if num % 2 == 0]
print(list2)

list3 = [x*2 for x in list1]
print(list3)


def is_prime(num):
    if num == 1:
        return False
    for n in range(2, num//2 + 1):
        if num % n == 0:
            return False
    return True


prime_list = [num for num in list1 if is_prime(num)]
prime_tuple = tuple(num for num in list1 if is_prime(num))  # need to cast to tuple/set/dict
print(prime_list)


def odd_even(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"


list_odd_even = [odd_even(x) for x in list1]
print(list_odd_even)

print(["Even" if num % 2 == 0 else "Odd" for num in list1])

print([x**2 for x in range(2, 11)])

print({num: "Even" if num % 2 == 0 else "Odd" for num in list1})
list4 = [[1, 2], [3, 4]]
print([y for x in list4 for y in x])