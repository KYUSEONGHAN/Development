# boj, 14487: 욱제는 효도쟁이야!!, python3

# 풀이1 -> 정렬을 이용한 풀이
import sys

input = sys.stdin.readline

def solve(l):
    return sum(sorted(l)[:-1])

if __name__ == '__main__':
    n = int(input())
    cost_list = list(map(int, input().split()))

    print(solve(cost_list))

# 풀이2 -> max 내장함수를 이용한 풀이
import sys

input = sys.stdin.readline

def solve(l):
    return sum(l) - max(l)

if __name__ == '__main__':
    n = int(input())
    cost_list = list(map(int, input().split()))

    print(solve(cost_list))