# https://www.acmicpc.net/problem/21866
# boj, 21866: 추첨을 통해 커피를 받자, python3
import sys

input = sys.stdin.readline

# 입력받은 학생이 추첨 대상자인지, 아닌지, 혹은 해커인지 구분하는 함수
def solve(scores: list) -> str:
    if sum(scores) < 100:
        return 'none'  # 추첨 대상자가 아니다

    # 각 문제당 최고 점수를 할당한 list
    max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
    # 입력 받은 점수와 문제의 최고 점수를 짝을 지어 비교하기 위해 zip으로 묶어서 할당
    score_zip = list(zip(scores, max_score))

    for student_s, max_s in score_zip:
        if student_s > max_s:
            return 'hacker'  # 헤커이다

    return 'draw'  # 추첨 대상자이다


if __name__ == '__main__':
    scores = list(map(int, input().split()))  # 학생이 각 문제에서 얻은 점수를 의미

    print(solve(scores))