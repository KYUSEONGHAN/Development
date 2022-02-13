# https://www.acmicpc.net/problem/10816
# boj, 10816: 숫자 카드 2, python3
import sys

input = sys.stdin.readline

def solve(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

if __name__ == '__main__':
    n = int(input())
    card_list = sorted(map(int, input().split()))
    m = int(input())
    sanggeun_list = list(map(int, input().split()))
    duplicate_cnt = {}
    result = [0] * m

    for i in card_list:
        if i not in duplicate_cnt:
            duplicate_cnt[i] = 1
        else:
            duplicate_cnt[i] += 1

    for x in range(len(sanggeun_list)):
        if solve(card_list, sanggeun_list[x], 0, n-1):
            result[x] = duplicate_cnt[sanggeun_list[x]]

    print(*result)
