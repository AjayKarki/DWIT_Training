"""
Write a function to compute the probability of the occurrence of these words in the file provided in the last assignment.

i) silver
ii) the
iii) a
"""
import re


def prob_cal(word, contents, total_occ):
    favourable = contents.count(word)
    return favourable / total_occ


file1 = open('shakespeare.txt', 'r')
content = file1.read()
content = content.lower()
list_words = re.findall("[a-z]+", content)
total_length = len(list_words)
prob_the = format(prob_cal("the", list_words, total_length), '.5f')
prob_silver = format(prob_cal("silver", list_words, total_length), '.5f')
prob_a = format(prob_cal("a", list_words, total_length), '.5f')
print("Silver Prob", prob_silver, "\nThe Prob", prob_the, "\nA Prob", prob_a)
