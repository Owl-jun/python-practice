def GuGu(num):
    result = []
    for i in range(1,10):
        result.append(num * i)
    
    if num > 9:
        return f'1~9단까지만 지원합니다. 지금 입력하신 값은 {num}입니다.'
    return result


print(GuGu(31))