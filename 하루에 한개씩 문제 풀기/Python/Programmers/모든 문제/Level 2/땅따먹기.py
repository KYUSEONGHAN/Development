# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# programmers, level2: 땅따먹기, python3
def solution(land):
    for j in range(1, len(land)):
        land[j][0] += max(land[j-1][1], land[j-1][2], land[j-1][3])
        land[j][1] += max(land[j-1][2], land[j-1][3], land[j-1][0])
        land[j][2] += max(land[j-1][3], land[j-1][0], land[j-1][1])
        land[j][3] += max(land[j-1][0], land[j-1][1], land[j-1][2])

    return max(land[-1])

if __name__ == '__main__':
    print(solution([[1,2,3,5], [5,6,7,8], [4,3,2,1]]))  # 16