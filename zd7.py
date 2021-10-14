N = int(input())
F = 1
S = 0

for i in range(1, N+1):
    F *= i
    S += F

print('Сумма факториалов чисел {0} равна {1}'.format(N, S))