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

dict_word_freq = dict(sorted(dict_word_freq.items(), key=lambda x: x[1], reverse=True))

word_count_list = []

for key, value in dict_word_freq.items():
    word_count_list.append(value)

print(word_count_list)
least_word_count_set = sorted(set(word_count_list), reverse=True)[-20:]
print(least_word_count_set)
most_word_count_set = sorted(set(word_count_list))[-20:]
print(most_word_count_set)

least_ten_dict = dict()
most_ten_dict = dict()
for key, value in dict_word_freq.items():
    if value in least_word_count_set:
        least_ten_dict[key] = value
        top_ten_least_occuring.write(key+" : " + str(value)+'\n')
    elif value in most_word_count_set:
        most_ten_dict[key] = value
        top_ten_most_occuring.write(key+" : " + str(value)+'\n')

    else:
        pass
print(least_ten_dict)
print(most_ten_dict)
top_ten_least_occuring.close()
top_ten_most_occuring.close()