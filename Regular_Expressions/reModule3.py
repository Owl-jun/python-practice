# 메타문자 2

# | = or
# ex ) p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)
# match = 'Crow'

# ^ = 문자열의 맨 처음과 일치함을 뜻함
# print(re.search('^Life','Life is too short'))

# $ = 문자열의 맨 끝과 일치함을 뜻함
# print(re.search('short$', 'Life is too short'))

# \A 줄이 여러개든 문자열의 맨처음과 매치됨

# \Z 줄이 몇개든간에 문자열의 마지막과 매치됨

# \b 단어 구분자 보통 단어는 공백에 의해 구분된다.
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# match = 'class'

# \B 공백이아닌 그냥 단어 구분 (앞 뒤에 공백이 하나라도 존재하면 None 반환)
# p = re.compile(r'\Bclass\B')
# print(p.search('abclassqq'))
# match = 'class'

# 그루핑 ()
# ABC 라는 문자열이 계속 반복되는지 조사하고 싶을 때에는 (ABC)+  << 'ABC' 라는 형태가 반복되면 매치


# 이름 + " " + 전화번호(하이픈포함) 형태 문자열 찾는 정규식

import re
p = re.compile(r'\w+\s\d+[-]\d+[-]\d+')
m = p.search('park 010-9501-1650')
print(m) 

# 이름이나 전화번호 부분만 뽑고 싶을땐?

p = re.compile(r'(\w+)\s((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-9501-1650')
print("이름 :",m.group(1))
print("전화번호 :",m.group(2))
print("국번 :",m.group(3)) # 인덱스는 바깥쪽 ()에서 안쪽 ()로 들어갈 수록 증가한다.

# 재참조 메타문자 \1 < 숫자는 그룹인덱스를 가르킨다.
p1 = re.compile(r'(\w+)\s+\1')
m1 = p1.search('Paris in the the spring').group()
print(m1)

# 그루핑된 문자열에 이름 붙이기
# (?P<name>) < 그룹안에 저거 삽입
p = re.compile(r'(?P<name>\w+)\s(?P<number>(?P<city>\d+)[-]\d+[-]\d+)')

m = p.search('OWL 010-9501-1650')
print(m.group('city'))
