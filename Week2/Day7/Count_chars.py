user_input = input("Enter any word")
count_dict = dict()
for ch in user_input:
    if ch not in count_dict.keys():
        count_dict[ch] = 1
    else:
        count_dict[ch] += 1
print(count_dict)

# print(user_input.count('p'))