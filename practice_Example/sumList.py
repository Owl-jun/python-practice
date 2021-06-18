# 리스트 총합 구하기

# 50점 이상 점수의 총합을 구하라.
a = [20,55,67,82,45,33,90,87,100,25]

for score in a:
    if score <= 50:
        a.remove(score)
    else: pass

print(a)

result = sum(a)    
print(result) # 왜 33은 안 없어지나?

# lst = []
# for i in a:
#     if i >= 50:
#         lst.append(i)
# print(lst)
# print(sum(lst))