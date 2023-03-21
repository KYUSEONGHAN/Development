# https://www.acmicpc.net/problem/10798
# boj, 10798: 세로읽기, Python3
def solve(data: list) -> str:
    result = ''

    for x in range(15):
        for y in range(5):
            # 배열의 범위를 벗어난 경우 예외처리
            try:
                result += data[y][x]
            except:
                pass

    return result

if __name__ == '__main__':
    # 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
    data = [list(input()) for _ in range(5)]

    print(solve(data))