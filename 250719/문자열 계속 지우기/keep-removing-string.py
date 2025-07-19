A = input()
B = input()

def find(source, target):
    for i in range(len(source) - len(target) + 1):
        if source[i:i+len(target)] == target:
            return i
    return -1

def erase(source, pos, length):
    return source[0:pos] + source[pos+length:]

while True:
    pos = find(A, B)
    if pos == -1:
        break
    else:
        A = erase(A, pos, len(B))

print(A)