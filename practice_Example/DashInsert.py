# 대쉬 인서트 함수
# 숫자로 구성된 문자열을 입력 받고 문자열 안에서 홀수가 연속되면 '-'를 추가, 짝수가 연속되면 '*'을 추가

def dashInsert(string):
    result = ''
    for i in range(len(string)):
        if i == len(string)-1: 
            result += string[i]
            return result
        if int(string[i]) % 2 == 0 and int(string[i+1]) % 2 == 0:
            result += string[i] + '*'
        elif int(string[i]) % 2 == 1 and int(string[i+1]) % 2 == 1:
            result += string[i] + '-'
        else: result += string[i]


print(dashInsert('4546793'))