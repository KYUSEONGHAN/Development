# 좋은단어인지 체크하는 함수
def good_word(word):
    # 스택 자료구조 선언
    stack = []

    # 입력받은 문자를 하나하나 반복문으로 순회
    for x in word:
        # stack에 값이 없다면
        if not stack:
            # 스택에 현재 요소 추가
            stack.append(x)
            # 아래 조건문 수행 안하도록
            continue
        # 현재 요소가 스택의 최신(top)과 다르다면
        if x != stack[-1]:
            # 스택에 추가
            stack.append(x)
        # 현재 요소가 스택의 최신(top)과 같다면
        elif x == stack[-1]:
            # pop -> 꺼낸다
            stack.pop()

    # 만약 스택에 값이 있다면 0을 반환
    if stack:
        return 0
    # stack에 값이 없다면 좋은단어이므로 1을 반환
    else:
        return 1

# main solution 함수
def solution(N):
    # 좋은단어수를 담는 list
    result = []

    # 반복할 변수만큼 반복
    for _ in range(N):
        # 좋은단어인지 체크하고 result list에 append (추가)
        result.append(good_word(str(input())))

    # 좋은 단어 수 반환
    return sum(result)

# 반복할 변수 입력받기
N = int(input())

# 정답 출력
print(solution(N))