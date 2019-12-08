
required_nos = []
for r in range(1500, 2701):
    if r % 7 == 0 and r % 5 == 0:
        required_nos.append(r)
print(required_nos)
