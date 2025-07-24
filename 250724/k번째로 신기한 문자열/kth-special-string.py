n, k, t = input().split()
n, k = int(n), int(k)
words = [input() for _ in range(n)]

# Please write your code here.

words.sort()

def is_same(t, word):
    l = len(t)
    return word[:l] == t

for word in words:
    if is_same(t, word):
        k -= 1
        if k == 0:
            print(word)

