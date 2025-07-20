string = input()

for char in string:
    if char.islower():
        print(char.upper(), end="")
    else:
        print(char.lower(), end="")
