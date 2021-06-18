# 피보나치 함수

# 1번 해결방안
def fib(n):

    result = [0,1]
    count = 0
    limit = n
    while True:
        a = result[count]+result[count+1]
        result.append(a)
        count += 1
        if count == limit-2:
            break
    return result

print(fib(10))

# 2번 해결방안

# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fib(n-2)+fib(n-1)

# for i in range(10):
#     print(fib(i))
