# boj, 1978 : 소수 찾기, PyPy3
import sys


def check_sosu(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True


def get_result():
    num_list = list(map(int, sys.stdin.readline().split(' ')))

    return sum(1 for i in num_list if check_sosu(i))


N = int(sys.stdin.readline())

print(get_result())