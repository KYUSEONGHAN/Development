# https://www.acmicpc.net/problem/4949
# boj, 4949: 균형잡힌 세상, python3

# 괄호검사 함수
def solve(word: str) -> str:  # 매개변수는 string형으로 받으며 함수의 반환형은 string형이라는 뜻.
    # stack list 초기화
    stack = []

    # word를 기준으로 반복문 순회
    for x in word:
        # x가 ( 또는 [ 일 시, stack에 추가
        if x == '(' or x == '[':
            stack.append(x)
        # ) 일 시,
        elif x == ')':
            # stack에 값이 있다면
            if stack:
                # stack의 값을 pop
                bracket = stack.pop()
                # pop한 값이 (이 아니면 () 매칭이 안되어서 잘못된 형식의 괄호이므로
                if bracket != '(':
                    return 'no'
            # stack게 값이 없다면 ) 로 시작되거나 ()) 와 같은 잘못된 형식의 괄호이므로
            else:
                # no를 반환
                return 'no'
        # x가 ] 일 시,
        elif x == ']':
            # stack에 값이 있다면
            if stack:
                # stack에 pop
                bracket = stack.pop()
                # pop한 값이 [이 아니면 [] 매칭이 안되는 잘못된 형식의 괄호이므로
                if bracket != '[':
                    # no를 반환
                    return 'no'
            # stack에 값이 없다면 ]이 첫번째로 들어가지므로 무조건 잘못된 형식의 괄호가 됨.
            else:
                return 'no'

    return 'yes' if not stack else 'no'

# 무한반복문
while True:
    # '.'을 기준으로 입력받은 후, 첫번째 인덱스만 word로 가져옴
    word = str(input().split('.')[0])

    # word가 비었을 경우, break
    if not word:
        break

    # 괄호검사 함수 호출
    print(solve(word))


