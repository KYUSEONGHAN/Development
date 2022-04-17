# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&#
# sw expert academy, d1: 2063. 중간값 찾기, python3
def solve(n: int, nums: list) -> int:
    return sorted(nums)[n//2]

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(n, nums))