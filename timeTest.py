import time

#시간 기록
print(time.asctime(time.localtime(time.time())))

# 1초 쉬었다가
time.sleep(1)

#현재시간만을 출력
print(time.ctime())

#양식대로 출력 time.localtime(time.time()) 이용 할 것.
print(time.strftime('%Y', time.localtime(time.time())))