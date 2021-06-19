# + - 번갈아가며 출력하기

# print('+와 -를 번갈아가며 출력합니다.')
# n = int(input('몇 개를 출력할까요?(정수값입력) : '))

# for i in range(n // 2):
#     print('+-', end='')

# if n % 2:
#     print('+', end='')

# *를 n개 출력하되 w개마다 줄바꿈 하기.

n, w = 14, 5

for i in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)