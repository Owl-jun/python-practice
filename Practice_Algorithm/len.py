# 직사각형 넓이로 변의 길이 구하기

# data = 32

# for i in range(1,data+1):
#     if i * i > data:
#         break
#     if data % i: continue
#     print(f'{i} x {data // i} = {i * (data//i)}')



# 난수 생성 하기 (로또번호)

import random

result = []
for i in range(6):
    print(f'{i+1}번째 번호는 무엇일까요? 두구두구두구(엔터 키를 누르시면 번호가 나옵니다)')
    i1 = input()
    r = random.randint(1,45)
    print(r)
    result.append(str(r))

print(f'최종 결과 : {",".join(result)}')