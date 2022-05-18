# https://www.acmicpc.net/problem/13866
# boj, 13866: 팀 나누기, python3
import sys

input = sys.stdin.readline

def solve(friend: list) -> int:
    return abs(sum(friends) - (max(friends) + min(friends)) * 2)

if __name__ == '__main__':
    friends = list(map(int, input().split()))

    print(solve(friends))