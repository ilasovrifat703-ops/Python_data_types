items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

classifier = {}

for pair in items:
    value, key = pair
    if key not in classifier:
        classifier[key] = []

for pair in items:
    value, key = pair
    classifier[key].append(value)

print(classifier)
