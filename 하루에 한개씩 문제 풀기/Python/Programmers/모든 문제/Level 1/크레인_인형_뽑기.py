# https://programmers.co.kr/learn/courses/30/lessons/64061
# programmers, level1: 크레인 인형 뽑기, python3
def solution(board: list, moves: list) -> int:
    stack = []
    answer = 0

    for move in moves:
        for x in range(len(board)):
            if board[x][move-1]:
                stack.append(board[x][move-1])
                board[x][move-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break

    return answer