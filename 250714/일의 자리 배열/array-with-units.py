A = [n for n in list(map(int, input().split()))]

for i in range(10 - len(A)):
    new_n = (A[i] + A[i+1]) % 10
    A.append(new_n)

for a in A:
    print(a, end=" ")