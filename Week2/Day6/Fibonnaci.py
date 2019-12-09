fib1, fib2 = 0, 1
num = int(input("How many you want to generate"))
for n in range(num):
    # fib1,fib2= fib2, fib1+fib2 if using this run loop upto num-2 and also print fib1 and fib2 at beginning
    fib2, fib1 = fib1, fib1+fib2
    print(fib2)
