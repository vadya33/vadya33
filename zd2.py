A = int(input())
B = int(input())

if B >= A:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(B, A+1):
        print(i)