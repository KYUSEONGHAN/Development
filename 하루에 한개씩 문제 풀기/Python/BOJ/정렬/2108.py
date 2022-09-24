# https://www.acmicpc.net/problem/2108
# boj, 2108: 통계학, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 산술평균을 구하는 함수, 소수점 이하 첫째 자리에서 반올림한 값을 반환
def get_avgs(n: int, nums: list) -> int:
    return int(round(sum(nums) / n, 0))

# 중앙값 구하는 함수
def get_middle(n: int, nums: list) -> int:
    return sorted(nums)[n // 2]

# 최빈값을 구하는 함수, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
def get_frequently_num(n: int, nums: list) -> int:
    if n == 1:  # n이 1이면 nums의 첫번째 요소가 최빈값이므로 바로 반환
        return nums[0]

    dict = {}  # nums list의 각 요소들이 얼마나 선언되었는지 확인하기 위한 dict 할당

    for num in nums:  # nums list for 반복문으로 순회
        if num not in dict:  # dict에 현재 반복문 요소가 할당되지 않았으면 할당해줌
            dict[num] = 1
        else:                # dict에 현재 반복문 요소가 할당되있다면 증감
            dict[num] += 1

    # 선언된 개수순 내림차슨 정렬 -> 선언된 수의 값 오름차순으로 dict 정렬
    sort_dict = sorted(dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)

    # 만일 정렬된 딕셔너리의 첫번째 키값의 벨류값과 두번째 키값의 벨류값이 같다면 최빈값이 여러개 있다는 의미.
    # 위와 같은 상황일시, 최빈값 중 두 번째로 작은 값을 반환
    # 위와 같은 상황이 아니라면, 최빈값의 키값을 반환
    return sort_dict[1][0] if sort_dict[0][-1] == sort_dict[1][-1] else sort_dict[0][0]

# 범위를 구하는 함수
def get_range(nums: list) -> int:
    return max(nums) - min(nums)

def solve(n: int, nums: list):
    print(get_avgs(n, nums))
    print(get_middle(n, nums))
    print(get_frequently_num(n, nums))
    print(get_range(nums))

if __name__ == '__main__':
    n = int(input())  # 수의 개수
    nums = [int(input()) for _ in range(n)]

    solve(n, nums)