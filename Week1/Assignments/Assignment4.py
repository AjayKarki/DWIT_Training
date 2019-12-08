number = int(input("Enter a number"))
list_of_divisors =[]
for n in range(1, number+1):
    if number % n == 0:
        list_of_divisors.append(n)
print(list_of_divisors)