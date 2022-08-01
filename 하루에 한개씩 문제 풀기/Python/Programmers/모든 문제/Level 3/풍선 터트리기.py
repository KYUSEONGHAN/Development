# https://school.programmers.co.kr/learn/courses/30/lessons/68646
# programmers, level3: 풍선 터트리기, python3
def solution(a: list):
    answer = 2

    if len(a) <= 2:
        return len(a)

    left, right = a[0], a[-1]

    for x in range(1, len(a)-1):
        if a[x] < left:
            left = a[x]
            answer += 1
        if a[-x-1] < right:
            right = a[-x-1]
            answer += 1

    return answer if left != right else answer - 1

if __name__ == '__main__':
    print(solution([9, -1, -5]))  # 3
    print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))  #6