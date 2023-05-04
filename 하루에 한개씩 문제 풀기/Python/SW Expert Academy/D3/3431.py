def solve(l: int, u: int , x: int) -> int:
    if x > u:  #  필요한 양보다 더 많은 운동을 하고 있다면 -1을 출력
        return -1
    return 0 if l <= x else l - x

T = int(input())

for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())
    print(f'#{test_case} {solve(l, u, x)}')