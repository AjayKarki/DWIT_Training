"""
Define a function is_even that will take a number x as input. If x is even, then return True. Otherwise,
return False.
"""


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


x = int(input("Enter number"))
print("Is Even?", is_even(x))