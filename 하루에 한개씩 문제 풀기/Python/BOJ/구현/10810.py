# https://www.acmicpc.net/problem/10810
# boj, 10810: 공 넣기, python3
def solve(n: int, m: int) -> list:
    balls = [0] * n

    for _ in range(m):
        start, end, num = map(int, input().split())
        balls[start-1:end] = [num] * (end - start + 1)

    return balls

if __name__ == '__main__':
    n, m = map(int, input().split())

    print(*solve(n, m))


"""ChatGPT code
n, m = map(int, input().split())

# 바구니의 초기 상태
baskets = [0] * n

# 공을 넣는 방법에 따라 바구니에 공을 넣음
for i in range(m):
    start, end, number = map(int, input().split())
    for j in range(start-1, end):
        baskets[j] = number

# 바구니에 들어있는 공의 번호 출력
for number in baskets:
    print(number, end=' ')
"""