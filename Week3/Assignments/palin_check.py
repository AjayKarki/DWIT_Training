# def is_palin(str):
#     if str == str[::-1]:
#         return True
#     else:
#         return False


list_str = ['madam', 'dad', 'myth', 'luffy']
# palin_str = []
# for str in list_str:
#     if is_palin(str):
#         palin_str.append(str)
# print(palin_str)

palin_words = list(filter(lambda x: x == x[::-1], list_str))
print(palin_words)