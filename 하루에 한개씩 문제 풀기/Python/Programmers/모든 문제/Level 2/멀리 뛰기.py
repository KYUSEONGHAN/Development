# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# programmers, level2: 멀리 뛰기, python3
def solution(n: int) -> int:
    d = [0] * 2001  # dp table 초기화
    d[1], d[2] = 1, 2

    #  dp bottom-up 수행
    for i in range(3, n+1):
        d[i] = (d[i-2] + d[i-1]) % 1234567

    return d[n]  # 결과값 반환

if __name__ == '__main__':
    print(solution(4))  # 5
    print(solution(3))  # 3