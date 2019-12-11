def greatest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


n1 = int(input("Enter Number 1"))
n2 = int(input("Enter Number 2"))
print(greatest(n1, n2))