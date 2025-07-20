string = input()

for char in string:
    if char.isalpha():
        print(char.lower(), end="")
    elif char.isdigit():
        print(char, end="")
    else:
        continue
