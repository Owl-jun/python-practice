# 문자열 바꾸기

a = 'a:b:c:d'
splitA = a.split(':')

result1 = a.replace(":","#")
result2 = "#".join(splitA)
print(result2)