#
# countries = ['Nepal', 'China', 'India']
# for country in countries:
#     print(country)
#
# for r in range(0, 10, 1):
#     print(r)
#
# list_num = []
# even_count = odd_count = zeros = 0
# for i in range(5):
#     num = int(input("Enter a number"))
#     if num == 0:
#         zeros += 1
#     elif num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     list_num.append(num)
# print(zeros, " Zeros\n", even_count, " Even Count\n", odd_count, " Odds ")
# # print(list_num)

num = int(input("Enter a number"))
div_seven = 0
for n in range(1, num + 1):
    if n % 7 == 0:
        div_seven += 1
        print(n, "is divisible by 7")
print("Total Divisible by 7 is ", div_seven)
