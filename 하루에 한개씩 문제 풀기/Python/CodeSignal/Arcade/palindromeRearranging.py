def solution(inputString: str) -> bool:
    dict = {}
    one_coin = 1

    for x in inputString:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for key, value in dict.items():
        if value % 2 == 1:
            one_coin -= 1
        if one_coin < 0:
            return False

    return True