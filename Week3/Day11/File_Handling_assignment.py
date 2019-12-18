import re

file1 = open('shakespeare.txt', 'r')
top_ten_most_occuring = open('top_ten_most.txt', 'w')
top_ten_least_occuring = open('top_ten_least.txt', 'w')

content = file1.read()
content = content.lower()
list_words = re.findall("[a-z]+", content)
set_words = set(list_words)
dict_word_freq = dict()

for word in list_words:
    if word in dict_word_freq.keys():
        dict_word_freq[word] += 1
    else:
        dict_word_freq[word] = 1

dict_word_freq = dict(sorted(dict_word_freq.items(), key=lambda x: x[1]))

word_count_list = []

for key, value in dict_word_freq.items():
    word_count_list.append(value)

least_word_count_set = sorted(set(word_count_list), reverse=True)[-20:]
most_word_count_set = sorted(set(word_count_list))[-20:]

least_ten_dict = dict()
most_ten_dict = dict()
for key, value in dict_word_freq.items():
    if value in least_word_count_set:
        if value not in least_ten_dict.keys():
            least_ten_dict[value] = [key]
        else:
            least_ten_dict[value].append(key)
    elif value in most_word_count_set:
        if value not in least_ten_dict.keys():
            most_ten_dict[value] = [key]
        else:
            most_ten_dict[value].append(key)
    else:
        pass

for key, value in least_ten_dict.items():
    least_ten_dict[key]= value[-3:]
    top_ten_least_occuring.writelines(str(key) + " - " + str(least_ten_dict[key])+'\n')
for key, value in most_ten_dict.items():
    least_ten_dict[key]= value[-3:]
    top_ten_most_occuring.writelines((str(key) + " - " + str(most_ten_dict[key]))+'\n')

top_ten_least_occuring.close()
top_ten_least_occuring.close()
