# 문자열 압축하기

data = 'aaabbcccccca'

def zipStr(data):
    result = ''
    cnt = 1
    for i in range(len(data)):
        if i == len(data)-1:
            result += data[i] + str(cnt)
            return result
        elif data[i] == data[i+1]:
            cnt += 1
        elif data[i] != data[i+1]:
            result += data[i] + str(cnt)
            cnt = 1

print(zipStr(data))