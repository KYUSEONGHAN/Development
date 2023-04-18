from typing import List

# 죽은 파리의 개수를 구하는 함수
def solve(graph: List[List[int]], n: int, m: int) -> int:
    result = 0  # 죽은 파리의 최대값을 담은 변수

    # 2중 for문 반복문으로 주어진 그래프 탐색
    for x in range(n-m+1):
        for y in range(n-m+1):
            dead_bug_cnt = sum([sum(graph[z][y:y+m]) for z in range(x, x+m)])
            result = max(result, dead_bug_cnt)

    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())  # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
    graph = [list(map(int, input().split())) for _ in range(n)]  # 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
    print(f'#{test_case} {solve(graph, n, m)}') # 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.