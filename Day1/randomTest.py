import random

# 0.0 ~ 1.0 사이의 실수중에서 난수 값을 돌려준다.
print(random.random())

# 1 ~ 10 사이의 정수중에서 난수 값을 돌려준다.
print(random.randint(1, 10))

# 리스트 값 중에 랜덤한 인덱스의 값을 추첨하여 보여주고 삭제하는 프로그램
def random_pop(data) :
    number = random.randint(0, len(data)-1)
    return data.pop(number)

data = [1,2,3,4,5]
while data: print(random_pop(data))

# choice 함수 활용

def random_pop2(data) :
    number = random.choice(data)
    data.remove(number)
    return number

data = [1,2,3,4,5]
while data: print(random_pop2(data))

# shuffle

data2 = [1,2,3,4,5,6,7,8,9]
random.shuffle(data2)
print(data2)
