# boj, 14487: 욱제는 효도쟁이야!!, python3
import sys

# input = sys.stdin.readline

def solve(l):
    return sum(sorted(l)[:-1])

if __name__ == '__main__':
    n = int(input())
    cost_list = list(map(int, input().split()))

    print(solve(cost_list))