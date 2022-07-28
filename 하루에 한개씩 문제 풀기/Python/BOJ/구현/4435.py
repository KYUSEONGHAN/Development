# https://www.acmicpc.net/problem/4435
# boj, 4435: 중간계 전쟁, python3
import sys

input = sys.stdin.readline

def solve(gandalf_army: list, sauron_army: list, x: int):
    gandalf_score = [1, 2, 3, 3, 4, 10]
    sauron_score = [1, 2, 2, 2, 3, 5, 10]

    gandalf = sum([x * y for x, y in zip(gandalf_army, gandalf_score)])
    sauron = sum([x * y for x, y in zip(sauron_army, sauron_score)])

    if gandalf > sauron:
        return f'Battle {x}: Good triumphs over Evil'
    elif gandalf < sauron:
        return f'Battle {x}: Evil eradicates all trace of Good'
    else:
        return f'Battle {x}: No victor on this battle field'

if __name__ == '__main__':
    t = int(input())  # 전투의 개수

    for x in range(1, t+1):
        gandalf_army = list(map(int, input().split()))
        sauron_army = list(map(int, input().split()))

        print(solve(gandalf_army, sauron_army, x))