text = input().lower().split()

count_words = {}
count_words = count_words.fromkeys(text,0)
for word in text:
    count_words[word]+=1

print(*sorted(count_words.items(), key = lambda x: x[1],reverse = True)[:5])
