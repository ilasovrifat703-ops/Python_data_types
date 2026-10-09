list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
list3 = list1 + list2
unique = []
non_unique = []

for i in list1:
    if i not in list2:
        unique.append(i)
    else:
        non_unique.append(i)

for i in list2:
    if i not in list1:
        unique.append(i)

print(unique,non_unique)
