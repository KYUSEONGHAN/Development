# https://school.programmers.co.kr/learn/courses/30/lessons/120861
# programmers, level0: 캐릭터의 좌표, python3
def up(start: list, position: list):
    if start[1] != (position[1]-1) / 2:
        start[1] += 1

def down(start: list, position: list):
    if start[1] != (position[1] - 1) / 2 * -1:
        start[1] -= 1

def left(start: list, position: list):
    if start[0] != (position[0] - 1) / 2 * -1:
        start[0] -= 1

def right(start: list, position: list):
    if start[0] != (position[0] - 1) / 2:
        start[0] += 1

def solution(keyinput: list, board: list) -> list:
    start = [0, 0]

    for x in keyinput:
        if x == 'up':
            up(start, board)
        elif x == 'down':
            down(start, board)
        elif x == 'left':
            left(start, board)
        elif x == 'right':
            right(start, board)

    return start

if __name__ == '__main__':
    print(solution(["left", "right", "up", "right", "right"], [11, 11]))  # [2, 1]
    print(solution(["down", "down", "down", "down", "down"], [7, 9]))  # [0, -4]