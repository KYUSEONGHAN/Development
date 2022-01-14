# boj, 11728: 배열 합치기, python3
import sys

def array_sum(n_list, m_list):
    return sorted(n_list+m_list)

def solve():
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    return array_sum(n_list, m_list)

if __name__ == '__main__':
    print(*solve())