from typing import List

def grade_average(l: List[int], start: int, end: int) -> float:
    score = round(sum(l[start-1:end]) / (end - start + 1), 2)

    if str(score)[-1] == '0':
        return str(score) + '0'
    return score

n, k = map(int, input().split())
si = list(map(int, input().split()))

for _ in range(k):
    a, b = map(int, input().split())
    print(grade_average(si, a, b))