# 더하기만 있는 계산기
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value += val

# 더하기 계산기 상속 후 마이너스 기능 추가 
class MoreCalculator(Calculator):
    def min(self,val):
        self.value -= val

# 100 이상의 결과값 제한
class MaxCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value >= 100:
            self.value = 100
            print('결과값은 100이상이 될 수 없습니다.')

cal = MaxCalculator()
cal.add(50)
cal.add(60)
print(cal.value)