# Duplicate Numbers
# 입력 받은 데이터가 0~9사이의 숫자를 한번씩만 사용했다면 True , 그 외는 False

data = ['0123456789', '01234', '01234567890', '6789012345', '012322456789']

def dupNum(data):
    setList = []
    for i in data:
        if i not in setList:
            setList.append(i)
        else: return False
    return len(setList) == 10

print(dupNum(data[0]))
