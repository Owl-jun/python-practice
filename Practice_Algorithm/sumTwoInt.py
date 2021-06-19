# a ~ b 정수의 합 구하기

# a , b = 10 , 22

# if a > b:
#     a, b = b, a

# sum = 0
# for i in range(a, b):
#     print(f"{i} + ", end='')
#     sum += i

# print(f'{b} = ', end="")
# sum += b
# print(sum)

# 양수 값만 입력 받기.

while True:
    n = int(input("n값을 입력하세요 (n은 양수값이어야만 합니다.) : "))
    if n > 0 :
        break
    else :
        print(f"양수 값을 입력하세요 현재 입력하신 값은 {n}으로 양수가 아닙니다.")

sum = 0

for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum} 입니다.')