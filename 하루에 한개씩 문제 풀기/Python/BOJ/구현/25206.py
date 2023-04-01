# https://www.acmicpc.net/problem/25206
# boj, 25206: 너의 평점은, python3
def solve(data: list) -> float:
    dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
    grade_score, total = 0, 0

    for x in data:
        _, score, grade = x
        if grade != 'P':
            total += float(score)
            grade_score += float(score) * dict[grade]

    return round(grade_score / total, 6)

if __name__ == '__main__':
    # 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
    data = [list(map(str, input().split())) for _ in range(20)]

    print(solve(data))