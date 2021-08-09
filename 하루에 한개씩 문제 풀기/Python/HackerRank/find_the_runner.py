# hackerrank, find the runner, python3
def solve(arr):
    return sorted(set(arr))[-2]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr))