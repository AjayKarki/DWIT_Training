text = input("Enter a string")
list_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = consonant_count = 0
for chars in text:
    if chars in list_vowel:
        vowel_count += 1
print("Vowel: ", vowel_count, "\nConsonant: ", len(text)-vowel_count)