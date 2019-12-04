# # Note  [::-1] reverse list
# # Append list
# # indexed, mutable, duplication, multiple data types
# a = [1, 2, 3, 4, 5, 6]
# a.append(7)
# # DOne list operations

# Tuples
# Non Mutable

# Sets
# non-indexed
# mutable
# no item duplication
# We can also use bitwise operator for union intersection

# Dictionary
co_cap = {
    "Nepal": "KTM",
    "Bhutan": "Thimpu",
    "Afgan": "Kabul",
    "India": "New Delhi",
    "China": "Beijing",
    "Pakistan": "Karachi"
}
print(co_cap['Nepal'])
co_cap["Maldives"] = 'Male'
# print(co_cap)
countries = co_cap.keys()
capitals = co_cap.values()
print(list(countries))
print(capitals)
print(sorted(co_cap.values(), reverse=True))
print(co_cap.get("Nepal"))
print(len(co_cap))