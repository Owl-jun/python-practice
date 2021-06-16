import random

result = []

while len(result) < 6 :
    num = random.randint(1, 45) # 1 ~ 45 사이의 난수 발생
    if num not in result :
        result.append(num)

print(result)