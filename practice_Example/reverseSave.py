# 역순저장

# with open('./practice_Example/abc.txt', 'r') as f:
#     read = f.readlines()
#     for i in range(len(read)):
#         with open('./practice_Example/cba.txt', 'a') as f1:
#             f1.write(read[-(i+1)])
        

# 2번

with open('./practice_Example/abc.txt', 'r') as f:
    read = f.readlines()
    read.reverse()
with open('./practice_Example/abc.txt', 'w') as f:
    for line in read:
        line = line.strip()
        f.write(line)
        f.write('\n')