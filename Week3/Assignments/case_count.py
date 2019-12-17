def case_count(str):
    upper_count = 0
    lower_count = 0
    for ch in str:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
        else:
            pass  # for ignoring other non alphabets
    return upper_count, lower_count


sent = input("Enter a sentence")
u_count, l_count = case_count(sent)
print("No. of Upper case characters :", u_count, "No. of Lower case Characters :", l_count)
