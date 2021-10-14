N = int(input())
U = N-1

for i in range(U, -1, -1):
    for j in range(N - U, 0, -1):
        print(j, end=" ")
    print(" ")
    U -= 1