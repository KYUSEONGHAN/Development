# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# programmers, level2: 스킬트리, python3
def solution(skill: str, skill_trees: list) -> int:
    # priority: 주어진 스킬 문자열의 우선순위를 담는 딕셔너리
    answer, priority = len(skill_trees), {x: i for i, x in enumerate(skill)}

    for x in skill_trees:  # 스킬트리 요소로 for문 반복
        match = 0  # 스킬이 맞는 순서를 담은 변수

        for y in x:
            if y in skill:  # skill_trees list 요소에 skill 문자열의 요소가 포함된다면
                if priority[y] == match:  # 우선순위에 맞게 차례대로 나왔을 시,
                    match += 1    # 다음 우선순위가 나오도록 match += 1
                else:  # 우선순위에 맞지않게 나왔을 시,
                    answer -= 1  # 주어진 skiil_trees list의 개수에 -1
                    break        # 현재 반복문 탈출

    return answer

if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2