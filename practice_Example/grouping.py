# 정규 표현식 그루핑

string ="""
park 010-0000-0099
kim 010-9909-7789
lee 010-8789-7768
"""

# 휴대폰 뒷자리 번호를 #### 으로 바꾸는 프로그램

import re
p = re.compile("(\d{3}[-]\d{4})[-]d{4}")
result = p.sub("\g<1>-####",string)

print(result)
# ??
