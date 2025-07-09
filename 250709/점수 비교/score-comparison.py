a_eng, a_math = map(int, input().split())
b_eng, b_math = map(int, input().split())

if a_eng > b_eng and a_math > b_math:
    print(1)
else:
    print(0)