# 전방 탐색
import re

p = re.compile('.+(?=:)')
m = p.search('http://naver.com')
print(m)

# (?=) < 긍정형 전방 탐색기법, ':' 문자가 소비되는걸 막아준다.
# (?!) < 부정형 전방 탐색기법, '' 지정한 문자가 매치되지않아야하며 문자가 소비되지 않음

# .*[.](?!bat$|exe$).*$ < \n을 제외한 모든문자가 0회이상 반복 '.'한개 bat or exe 로 문자가 끝나면 제외, 그 외의 결과는 모두 매칭

# 문자열 바꾸기
# sub 메서드 p.sub('바꿀문자열', '대상문자열', '바꿀횟수'(ex:count=1))
# subn 은 튜플 값으로 돌려준다.

p = re.compile(r'(?P<name>\w+)\s(?P<number>(\w+)[-]\w+[-]\w+)')
print(p.sub("\g<number> \g<name>", "park 010-1234-1234")) # sub메서드의 참조구문 \g (그룹)<그룹이름> 의 형식
print(p.sub("\g<2> \g<1>","park 010-1234-1234")) # 숫자로 해도 동일

# sub 메서드 함수에 활용

def hexrepl(match):
    value = int(match.group()) # 매치된 문자를 정수형으로 변환
    return hex(value) # 값을 16진수로 리턴

p1 = re.compile(r'\d+') # 정수 값만 매칭하겠다.
m1 = p1.sub(hexrepl, "Call 65490 for printing, 49152 for user code.")
print(m1)

# greedy , non-greedy

s = '<html><head><title>Title</title>'
print(re.match('<.*?>', s).group())