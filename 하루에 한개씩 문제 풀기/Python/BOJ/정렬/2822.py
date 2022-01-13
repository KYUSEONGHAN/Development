# boj, 2822:점수 계산, python3
import sys

def solve(score):
    l = sorted(score, reverse=True)[:5]
    result = [score.index(x)+1 for x in l]

    print(sum(l))
    print(*sorted(result))

if __name__ == '__main__':
    score = [int(sys.stdin.readline()) for _ in range(8)]

    solve(score)