n = int(input())

# Please write your code here.
def func(n):
    if n % 2 == 0:
        str_n = str(n)
        n1 = int(str_n[0])
        n2 = int(str_n[1])
        if (n1 + n2) % 5 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(func(n))