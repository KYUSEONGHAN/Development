# 수정 전
# boj, 1009 : 분산처리, python3
import sys

T = int(input())
ab_list = []
result = []

for _ in range(T):
    ab = list(map(int, input().split()))
    ab_list.append(ab)

for i in ab_list:
    bunsan = i[0] ** i[1]
    bunsan %= 10
    result.append(bunsan)

print("\n".join(map(str, result)))


# 수정 후
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    # 1의 자리 수가 4와 9인 경우는 반복 되는 값이 2개 이므로 제곱수를 2로 나누어서
    # 홀수 승과 짝수 승을 비교하여 계산
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        # 4개씩 싸이클이 돌 때 마다 자기 자신이 나오므로 나누었을때 나머지가 0이라면 자기 자신을 출력
        b = b % 4
        if b == 0:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)