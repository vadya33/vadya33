N, K = int(input()), int(input())

f1, f2 = 1, 1
s = 0
d = 0

for i in range(3, N+1):
    if i <= K:
        d = f1 + f2

    s = f1 + f2
    f1 = f2
    f2 = s
print(s - d)