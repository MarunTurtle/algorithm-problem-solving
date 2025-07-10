gender = int(input())
age = int(input())

if age >= 19:
    if gender == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    if gender == 0:
        print("BOY")
    else:
        print("GIRL")