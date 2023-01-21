# https://school.programmers.co.kr/learn/courses/30/lessons/120885
# programmers, level0: 이진수 더하기, python3
def solution(bin1: str, bin2: str) -> str:
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

if __name__ == '__main__':
    print(solution("10", "11"))  # "101"