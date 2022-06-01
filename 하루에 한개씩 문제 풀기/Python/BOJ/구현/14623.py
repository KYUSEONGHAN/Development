# https://www.acmicpc.net/problem/14623
# boj, 14623: 감정이입, python3
def solve(b1: str, b2: str) -> str:
    b1_to_10 = int(b1, 2)  # 2진수 -> 10진수 변환
    b2_to_10 = int(b2, 2)

    return bin(b1_to_10 * b2_to_10)[2:]  # 10진수 -> 2진수로 변환

if __name__ == '__main__':
    b1 = input()
    b2 = input()

    print(solve(b1, b2))