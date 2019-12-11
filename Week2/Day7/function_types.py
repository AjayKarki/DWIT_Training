def sum_diff(num1, num2):
    """Example for multi value return"""
    return num1 + num2, num1 - num2


sum_num,  diff_num = sum_diff(5, 3)
print(sum_num, diff_num)

""" 
If a function is called as
greater_num(num2=4, num1=1) instead of  greater_num(num1, num2)
then it is the case of passing Keyword Args not Kwargs
Example of use of kwargs : In machine learning, pandas where there are tons of args
"""
"""
Aggregated arguments
Two types:
1. args
2. kwargs
"""


def sum_num_args(* args):
    """Example of args"""
    print(type(args))
    return sum(args)


print(sum_num_args(1, 2, 3, 4, 5, 6))

"""
Default(Optional) Arguments
"""


def default_args_example(num1, num2, num3 = 0):
    return num1 + num2 + num3


print(default_args_example(1, 2, 3))
print(default_args_example(1, 2))