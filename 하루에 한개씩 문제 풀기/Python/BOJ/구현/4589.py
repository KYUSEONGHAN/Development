# https://www.acmicpc.net/problem/4589
# boj, 4589: gnome sequencing, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# (shortest to longest) or (longest to shortest) 또는 그 외의 경우인지 판별하는 함수
def solve(l: list) -> str:
    if l[0] == max(l):
        compare_l = sorted(l, reverse=True)
    elif l[0] == min(l):
        compare_l = sorted(l)
    else:
        return 'Unordered'

    return 'Ordered' if l == compare_l else 'Unordered'

if __name__ == '__main__':
    n = int(input())

    print('Gnomes:')

    for _ in range(n):
        datas = list(map(int, input().split()))

        print(solve(datas))