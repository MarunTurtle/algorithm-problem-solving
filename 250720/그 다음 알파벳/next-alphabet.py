l = input()
n = ord(l)

if l == 'z':
    n = ord('a')
else:
    n += 1

print(chr(n))