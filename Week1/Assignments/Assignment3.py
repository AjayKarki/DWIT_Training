number = int(input("Enter a number"))
is_prime = 1
for n in range(2, number//2+1):    # not necessary to goto the number reaching upto half of the number is fine
    if number % n == 0:
        is_prime = 0
        break
if is_prime:
    print("Usr input number is prime")
else:
    print("User input number is not prime")