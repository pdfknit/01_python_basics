import math

N = int(input('Введите N:\n'))
num_02 = (num for num in range(1, N + 1, 2))

for _ in range(1, (math.ceil(N / 2 + 1))):
    print(next(num_02))
