# https://programmers.co.kr/learn/courses/30/lessons/67256
# programmers, level1: 키패드 누르기, python3
def solution(numbers: list, hand: str) -> str:
    left, right = [1, 4, 7], [3, 6, 9]
    left_finger, right_finger = 10, 12
    answer = ''

    for number in numbers:
        if number == 0:
            number = 11
        # 왼속으로 칠 수 있는 경우
        if number in left:
            answer += 'L'
            left_finger = number
        # 오른손으로 칠 수 있는 경우
        elif number in right:
            answer += 'R'
            right_finger = number
        # 가운데 열인 경우
        else:
            # 왼손이 더 가까운 경우
            if sum(divmod(abs(left_finger-number), 3)) < sum(divmod(abs(right_finger-number), 3)):
                answer += 'L'
                left_finger = number
            # 오른손이 더 가까운 경우
            elif sum(divmod(abs(left_finger-number), 3)) > sum(divmod(abs(right_finger-number), 3)):
                answer += 'R'
                right_finger = number
            # 왼손과 오른손의 거리가 같을 경우 주로 사용하는 손으로 선택
            else:
                if hand == 'left':
                    answer += 'L'
                    left_finger = number
                else:
                    answer += 'R'
                    right_finger = number

    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))   # "LRLLRRLLLRR"
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))     # "LLRLLRLLRL"