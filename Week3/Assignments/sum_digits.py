def sum_of_digits(*args):
    sum_of = dict()
    for num in args:
        sums = 0
        for i in str(num):
            sums += int(i)
        sum_of[num] = sums
    return sum_of


print(sum_of_digits(123, 456, 778))