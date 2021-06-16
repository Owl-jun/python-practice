import re
# 사용 방법 (컴파일)
# p = re.compile('ab*')

# 검색
# print(p.match('abbb')) # 문자열의 처음부터 정규식과 매치되는지 조사
# print(p.search('abbbb')) # 문자열 전체를 검색하여 정규식과 매치되는지 조사
# print(p.findall('abbbb')) # 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
# p.finditer('abb') # 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.

# match 사용 예시
p = re.compile('[a-z]+')
m = p.match("python")
if m:
    print('Match found : ', m.group())
else:
    print('No Match')

# search 사용 예시
m2 = p.search("3 python")
print(m2.group())

# findall 사용 예시
result = p.findall("life is too short")
print(result)

# finditer 사용 예시
result2 = p.finditer("life is too short")
print(result2)
for i in result2: print(i)

# match / search 메서드
print(m.group()) # 매치된 문자열을 돌려줌
print(m.start()) # 매치된 문자열의 시작 인덱스값
print(m.end()) # 매치된 문자열의 마지막 인덱스값
print(m.span()) # (시작,끝) 형식의 튜플값

# 축약형
m3 = re.match('\w+', "python")
print(m3.group())