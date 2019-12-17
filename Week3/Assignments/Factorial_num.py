def factorial_n(num):
    facto = 1
    for n in range(2, num + 1):
        facto *= n
    return facto


number = int(input("Enter the number"))
while number <= 0:
    number = int(input("Enter Positive number"))
print("Factorial of ", number, "is", factorial_n(number))
