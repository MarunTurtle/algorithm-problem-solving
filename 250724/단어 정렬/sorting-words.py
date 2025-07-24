n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

words.sort()

for word in words:
    print(word)