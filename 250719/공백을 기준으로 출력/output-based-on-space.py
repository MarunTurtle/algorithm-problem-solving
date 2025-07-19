sentence = ""

for _ in range(2):
    words = list(map(str, input().split()))
    for word in words:
        sentence += word

print(sentence)