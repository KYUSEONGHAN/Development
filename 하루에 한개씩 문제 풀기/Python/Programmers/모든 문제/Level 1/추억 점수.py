def solution(name, yearning, photo):
    name_yearning = dict(zip(name, yearning))  # 이름과 그리움 점수를 딕셔너리로 매핑

    result = []  # 사진들의 추억 점수를 담을 리스트

    for p in photo:
        total_score = 0  # 사진의 추억 점수

        for person in p:
            if person in name_yearning:  # 사진 속 인물이 그리워하는 사람 중에 있다면
                total_score += name_yearning[person]  # 그리움 점수를 합산

        result.append(total_score)

    return result
