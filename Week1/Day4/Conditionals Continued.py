# num = int(input("Enter a number"))
# if num > 0:
#     print("Positive")
# elif num ==0:
#     print("Zero")
# else:
#     print("Negative")
#

first_no = int(input("Enter 1st number"))
second_no = int(input("Enter 2nd number"))
operator = input("Input Operation")
if operator == '+':
    print(first_no + second_no)
elif operator == '-':
    print(first_no - second_no)
elif operator == '*':
    print(first_no * second_no)
elif operator == '/':
    print(first_no / second_no)
elif operator == '**':
    print(first_no ** second_no)
elif operator == '//':
    print(first_no // second_no)
elif operator == '%':
    print(first_no % second_no)
else:
    print("Invalid Operator")

