# Approach 1
number = input("Enter a number")
sum = 0
for n in number:
    sum += int(n)**len(number)
if sum == int(number):
    print("Armstrong")
else:
    print("Not Armstrong")

# Approach 2
# sum = 0
# number = int(input("Enter a number"))
# copy_number = number
# while number != 0:
#     digit = number % 10
#     sum = digit ** len(str(copy_number))
#     number //= 10
# if sum == copy_number:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
