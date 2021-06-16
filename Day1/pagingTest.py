#게시판 페이징하기

def getTotalPage(n1,n2):
    if n1 % n2 == 0:
        return n1//n2
    else :
        return n1//n2 +1

print(getTotalPage(30,10))