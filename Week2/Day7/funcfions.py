"""
Pass By reference - Collections
Pass By Value - Basic data types
"""


def print_hello():
    """This is a sample function. It prints Hello World !!!"""
    print("Hello from the other side !!!")
    return


def cal_sum(num1, num2):
    """Function to return sum of numbers"""
    sum_number = num1 + num2
    return sum_number


print_hello()
ans = cal_sum(2, 2)
print(ans)


def pass_by_value(a):
    """Example for pass by value"""
    a = 3
    return


num = 2
print(num)
pass_by_value(num)
print(num)


def pass_by_reference(list_num):
    """Example for pass by reference"""
    list_num.append(3)
    return


num_list = [1, 2, 3, 4]
pass_by_reference(num_list)
print(num_list)