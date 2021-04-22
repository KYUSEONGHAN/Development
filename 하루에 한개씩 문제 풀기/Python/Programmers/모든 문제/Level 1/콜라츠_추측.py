# programmers, phase1 : 콜라츠 추측, python3
def solution(num):
    cnt = 0

    while True:
        if num == 1:
            break
        if cnt == 500:
            break
        if num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1

    return cnt if cnt != 500 else -1


# 최적코드
#  - , - , - , 강준기 , - 외 7 명 님 코드 참고
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1
