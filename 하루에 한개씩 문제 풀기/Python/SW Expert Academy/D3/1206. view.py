# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# programmers, d3: [S/W 문제해결 기본] 1일차 - View, python3
def solve(index:int, nums: list):
    result = 0

    if nums[0] > nums[1] and nums[0] > nums[2]:
        result += nums[0] - max(nums[1], nums[2])
    if max(nums[0], nums[1], nums[2], nums[3]) == nums[1]:
        result += nums[1] - max(nums[0], nums[2], nums[3])
    if max(nums[-2], nums[-1], nums[-3], nums[-4]) == nums[-2]:
        result += nums[-2] - max(nums[-1], nums[-3], nums[-4])
    if nums[-1] > nums[-2] and nums[-1] > nums[-3]:
        result += nums[-1] - max(nums[-2], nums[-3])

    for x in range(2, len(nums)-2):
        if max(nums[x], nums[x-1], nums[x-2], nums[x+1], nums[x+2]) == nums[x]:
            result += nums[x] - max(nums[x-1], nums[x-2], nums[x+1], nums[x+2])

    return '#' + str(index), result

if __name__ == '__main__':
    # 총 10개의 테스트케이스가 주어진다,
    for index in range(1, 10+1):
        # 한 테스트 케이스의 입력 데이터 수
        n = int(input())
        nums = list(map(int, input().split()))
        print(*solve(index, nums))