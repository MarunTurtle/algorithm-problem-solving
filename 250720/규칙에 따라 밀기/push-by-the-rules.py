word = input()
command = list(input())

def left(word):
    return word[1:] + word[0]

def right(word):
    return word[-1] + word[0:-1]

for c in command:
    if c == 'L':
        word = left(word)
    else:
        word = right(word)

print(word)