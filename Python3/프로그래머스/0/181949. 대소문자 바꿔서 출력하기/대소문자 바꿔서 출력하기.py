str = input()
result = ""

for i in range(len(str)):
    if str[i].isupper():
        result += str[i].lower()
    else:
        result += str[i].upper()
        
print(result)