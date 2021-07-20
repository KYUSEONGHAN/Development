# boj, 10974 : 모든 순열, python3
# 브루트포스 알고리즘
import sys

def dfs(depth):
    global answer

    if depth == n:
        answer.append([num for num in check])
    else:
        for i in range(n):
            if i + 1 in check:
                continue
            check[depth] = i + 1
            dfs(depth + 1)
            check[depth] = 0

if __name__ == '__main__':
    answer = []
    n = int(sys.stdin.readline())
    check = [0] * n
    dfs(0)

    for case in answer:
        print(*case)