# tab 을 공백 4개로 변환하는 프로그램

import sys


src = sys.argv[1]
dst = sys.argv[2]

with open(src,'r') as f:
    content = f.read()

space = content.replace('\t',' '*4)

with open(dst,'w') as f2:
    f2.write(space)



