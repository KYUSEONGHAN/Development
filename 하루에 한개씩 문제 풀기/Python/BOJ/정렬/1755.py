# https://www.acmicpc.net/problem/1755
# boj, 1755: 숫자 놀이, python3
import sys

input = sys.stdin.readline

def solve(m, n):
    number_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    nums = [list(map(int, str(x))) for x in range(m, int(n)+1)]
    convert_dict = {}

    for x in nums:
        word = ""
        num = ""
        for y in x:
            word += number_dict[y]
            num += str(y)
        convert_dict[num] = word

    sort_dict = sorted(convert_dict.items(), key=lambda x: x[1])
    result = [int(x[0]) for x in sort_dict]
    tmp = 10

    for x in range(0, len(result), 10):
        print(*result[x:tmp])
        tmp += 10

if __name__ == '__main__':
    m, n = map(str, input().split())

    solve(int(m), n)