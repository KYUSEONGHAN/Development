# programmers, phase2:h-index, python3
# 정렬 알고리즘
def solution(citations):
    l = sorted(citations, reverse=True)

    for i, target in enumerate(l):
        if target <= i:
            return i

    return len(l)