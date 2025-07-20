string = input()

for char in string:
    if char.isalpha():
        print(char.upper(), end="")