# programmers, level1: 부족한 금액 계산하기, python3
def solution(price, money, count):
    price = sum([x for x in range(1, count+1)]) * price

    if price <= money:
        return 0

    return price - money