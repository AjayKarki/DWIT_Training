def max_num(f_num, s_num, t_num):
    # Alternatively
    # if f_num > s_num and f_num > t_num:
    #     return f_num
    # elif s_num > t_num:
    #     return s_num
    # else:
    #     return t_num
    return max(f_num, s_num, t_num)


first_num = int(input("Enter 1st number"))
second_num = int(input("Enter 2nd number"))
third_num = int(input("Enter 3rd number"))
print("Max number is", max_num(first_num, second_num, third_num))
