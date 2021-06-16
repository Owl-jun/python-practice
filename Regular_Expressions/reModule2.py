import re

# 컴파일 옵션
'''
옵션이름    약어    설명
DOTALL      S       dot 문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.
IGNORECASE  I       대,소문자 관계없이 매치한다.
MULTILINE   M       여러줄과 매치한다. (메타문자 사용과 관계가 있는 옵션)
VERBOSE     X       정규식을 보기 편하게 만들 수도 있고, 주석 등을 사용할 수 있는 verbose 모드를 사용한다.

사용 방법 => re.DOTALL & re.S  
'''

# DOTALL, S (줄바꿈이 있어도 찾아)
p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

# IGNORECASE, I (대소문자 구분없이 매치)
p1 = re.compile('[a-z]+', re.I)
m1 = p1.match('abC')
print(m1)

# MULTININE, M (컴파일 규칙을 각 줄마다 설정)
p2 = re.compile("^python\s\w+", re.M) # python 이라는 단어가 처음에 등장해야하고 \s(공백)하나가 있고 아무글자가 반복되어 나오는 것을 찾아라!
data = """python one
python two
you need python
python three
"""
m2 = p2.findall(data)
print(m2)

# VERBOSE, X 주석 , 줄바꿈을 통해 보기 쉽게 정규표현식 사용가능
p3 = re.compile(r'''
&[#]                # Start of a numeric entity reference
(   
    0[0-7]+         # Octal form
    |[0-9]+         # DEcimal form
    |x[0-9a-fA-F]+  # Hexadecimal form
)
;
''',re.VERBOSE)

# 백슬래쉬 \ 문제

# \section < 이라는 문자를 찾기 위한 정규식을 만든다고 가정할때,
# \\ < 이런식으로 두번 사용해야 한다. 안그러면 \s = space 로 인식해버림.
# r'\section' => r을 사용하면 문자열 그대로 인식하게된다.