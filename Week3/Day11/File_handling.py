import string

# file1 = open('test.txt', "a")
# # list_sent = ['I am ajay karki', 'I learn python','i live in baneshwor']
# # file1.writelines([x + '\n' for x in list_sent])
# # file1.close()
#
# co_cap = {"Nepal": "KTM", "India": "New Delhi"}
# # for key,val in co_cap.items():
# #     file1.write(key + " " + val + '\n')
#
# file1.writelines([key + ',' + val + '\n' for key, val in co_cap.items()])
# [file1.write(key + " " + val + '\n') for key,val in co_cap.items()]
# file1.close()

# file1 = open('test.txt', 'r')
# content = file1.read()
# # content = file1.readline()
# # content = file1.readlines()
# print(content)
# file1.close()

"""
with open('text.txt','r') as f:
    con = f.read()
    print(con)
with this method we don't need to close the file
"""
#
# file1 = open('test.txt', 'r')
# line = file1.readline()
# while line != "":
#     co, cap = line.split(',')
#     print("Country:" , co,"Captial:", cap)
#     line =file1.readline()
# file1.close()

import re

file1 = open('shakespeare.txt', 'r')
content = file1.read()
content = content.lower()
list_words = re.findall("[a-z]+", content)
set_words = set(list_words)
dict_word_freq = dict()
# for word in set_words:
#     dict_word_freq[word] = list_words.count(word)
# print(dict_word_freq.sort())


for word in list_words:
    if word in dict_word_freq.keys():
        dict_word_freq[word] += 1
    else:
        dict_word_freq[word] = 1
