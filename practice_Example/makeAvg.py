# 파일 읽어와서 평균값 구하여 다른 파일에 작성하기

result = []
with open('./practice_Example/sample.txt', 'r') as f:
    read = f.readlines()
    for i in range(len(read)):
        result.append(int(read[i].strip()))

sumresult = sum(result)
avgresult = sumresult / len(result)

with open('./practice_Example/result.txt', 'w') as f1:
    f1.write(f'총합 : {sumresult}\n 평균 : {avgresult}')