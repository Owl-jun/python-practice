# 3과 5의 배수 합하기 프로그램

# 1번 풀이
# lst = []
# for i in range(1,1000):
#     if i % 3 == 0:
#         lst.append(i)

# for i in range(1,1000):
#     if i % 5 == 0 and i not in lst:
#         lst.append(i)

# print(sum(lst))

# 최적화 코드 제일 짧게 만들어보기

# result = 0
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 ==0:
#         result += i
# print(result)

# 응용 (용이한 수정)

n1, n2 = map(int, input('배수를 합할 숫자 두개를 입력하세요 (공백으로 분리) : ').split())
result = 0
for i in range(1,1000):
    if i % n1 == 0 or i % n2 ==0:
        result += i
print(result)
