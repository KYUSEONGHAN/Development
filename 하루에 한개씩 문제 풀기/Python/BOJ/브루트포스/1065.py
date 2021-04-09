# boj, 1065 : 한수, python3
N = int(input())

def hansu(num):
    cnt = 0
    for i in range(1,num+1):
        if i <= 99:
            cnt += 1
        else:
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1
    print(cnt)

hansu(N)