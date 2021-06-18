# 리스트 계산기

class Calculator():
    def __init__(self,list):
        self.list = list
    def sum(self):
        result = sum(self.list)
        return result
    def avg(self):
        result = sum(self.list)/len(self.list)
        return result


cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())