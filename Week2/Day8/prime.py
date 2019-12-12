def is_prime(num):
    for n in range(2, num//2+1):
        if num % n == 0:
            return False
    return True


number = int(input("Enter a number"))
print(is_prime(number))