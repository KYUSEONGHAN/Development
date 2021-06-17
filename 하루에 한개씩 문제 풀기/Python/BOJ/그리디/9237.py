# boj, 9237 : 이장님 초대, python3
# 그리디 알고리즘
import sys

def tree(l):
    return max([i+j+2 for i,j in enumerate(l)])


N = int(sys.stdin.readline())
t = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)

print(tree(t))