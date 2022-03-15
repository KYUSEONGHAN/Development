# https://www.acmicpc.net/problem/11723
# boj, 11723: 집합, python3
import sys

input = sys.stdin.readline

# s에 x를 추가한다. s에 x가 이미 있는 경우에는 연산을 무시한다.
def add(s, order):
    # set은 중복을 제거해서 x가 이미 있어도 알아서 무시됨.
    s.add(int(order[1]))

# s에서 x를 제거한다. s에 x가 없는 경우에는 연산을 무시한다.
def remove(s, order):
    # discard를 쓰면 remove와는 달리 x가 없는 경우에는 연산을 무시함.
    s.discard(int(order[1]))

# s에서 x가 있으면 1을, 없으면 0을 출력한다.
def check(s, order):
    if int(order[1]) in s:
        print(1)
    else:
        print(0)

# s에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
def toggle(s, order):
    if int(order[1]) in s:
        s.remove(int(order[1]))
    else:
        s.add(int(order[1]))

# s를 {1, 2,,,,,20}으로 바꾼다.
def all(s):
    return {i for i in range(1, 21)}

# s를 공집합으로 바꾼다.
def empty(s):
    return set()


def solve(orders):
    # 비어있는 공집합 s가 주어졌을 때,
    s = set()

    # m개의 줄에 수행해야 하는 연산들
    for _ in range(m):
        order = list(map(str, input().split()))

        if order[0] == 'add':
            add(s, order)
        elif order[0] == 'remove':
            remove(s, order)
        elif order[0] == 'check':
            check(s, order)
        elif order[0] == 'toggle':
            toggle(s, order)
        elif order[0] == 'all':
            s = all(s)
        elif order[0] == "empty":
            s = empty(s)


if __name__ == '__main__':
    # 수행해야 하는 연산의 수
    m = int(input())

    solve(m)
