A = input()
B = input()

pattern_exists = True

while pattern_exists:
    pattern_exists = False
    for i in range(len(A) - len(B) + 1):
        if A[i:i + len(B)] == B:
            A = A[0:i] + A[i + len(B):]
            pattern_exists = True
            break
print(A)