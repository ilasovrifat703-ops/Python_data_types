items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

classifier = dict()
for pair in items:
    key,value = pair
    if key not in classifier:
        classifier[value] = []

for pair in items:
    value, key = pair
    classifier[key].append(value)

print(classifier)
