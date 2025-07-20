n = int(input())
letter = 'A'

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i):
        print(letter, end=" ")
        
        if letter == "Z":
            letter = "A"
        else:
            letter = chr(ord(letter) + 1)
    print()

        