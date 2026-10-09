items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

classifier = {items[i][1]: [] for i in range(len(items))}

for pair in items:
    value, key = pair
    classifier[key].append(value)

print(classifier)
