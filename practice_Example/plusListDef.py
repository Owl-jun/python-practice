# 리스트 더하기와 extend 함수

a = [1,2,3]
a1 = a + [4,5]

a.extend([4,5])

print(id(a))
print(id(a1))
print(a)

# + 를 사용할시 id값이 달라지고, extend 사용시 id값이 같다.