<<<<<<< HEAD
# 간단한 메모장 만들기 (feat.sys)

import sys

option = sys.argv[1] # 터미널 입력 중 makeMemo.py 를 제외하고 1번 인덱스 부분
content = sys.argv[-1] # 맨 마지막에 나온 문장

# 쓰기 , 보기 기능
if option == '-a':
    with open('memo.txt','a') as f:
        f.write(content)
elif option == '-v':
    with open('memo.txt','r') as f:
        view = f.read()
=======
# 간단한 메모장 만들기 (feat.sys)

import sys

option = sys.argv[1] # 터미널 입력 중 makeMemo.py 를 제외하고 1번 인덱스 부분
content = sys.argv[-1] # 맨 마지막에 나온 문장

# 쓰기 , 보기 기능
if option == '-a':
    with open('memo.txt','a') as f:
        f.write(content)
elif option == '-v':
    with open('memo.txt','r') as f:
        view = f.read()
>>>>>>> 841a45b7f3e1e93bd6003f812424a06fa1844960
        print(view)