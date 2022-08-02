def solution(people, limit):
    answer = 0

    people.sort()  # 몸무게 오름차순으로 정렬
    start, end = 0, len(people) - 1

    while True:
        if people[start] + people[end] > limit:
            end -= 1
            answer += 1
        else:
            start += 1
            end -= 1
            answer += 1
        if start > end:
            break
        elif start == end:
            if people[start] <= limit:
                answer += 1
            break

    return answer

if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))            # 3
    # 50 50 70 80 -> 100
    print(solution([70, 80, 50], 100))                # 3
    # 50 70 80 -> 100  50 50 70
    print(solution([40, 50, 150, 160], 200))          # 2
    # 40 50 150 160 -> 200
    print(solution([100, 500, 500, 900, 950], 1000))  # 3
    # 100 500 500 900 950 -> 1000