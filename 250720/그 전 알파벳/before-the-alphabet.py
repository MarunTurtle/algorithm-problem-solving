l = input()
n = ord(l)

if l == 'a':
    n = ord('z')
else:
    n -= 1

print(chr(n))