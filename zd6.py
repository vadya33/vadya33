N = int(input())
F = 1

for i in range(1, N+1):
    F *= i

print('Факториал числа {0} равен {1}'.format(N, F))