# 숫자의 총합 구하기

def sumNumbers():
    numbers = list(map(int, input("숫자입력 콤마(,)로 구분하여 입력 : ").split(',')))
    return sum(numbers)

print(sumNumbers())