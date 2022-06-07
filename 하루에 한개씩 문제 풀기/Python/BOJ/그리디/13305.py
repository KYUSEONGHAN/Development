# https://www.acmicpc.net/problem/13305
# boj, 13305: 주유소, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 구하는 함수
def solve(lengths: list, prices: list) -> int:
    gas_station = list(zip(lengths, prices[:-1]))   # 주유소 정보인 도로 길이, 리터당 가격을 zip 함수로 연결, 마지막 인덱스는 불필요 제외.
    cost = gas_station[0][1]                        # 첫뻔째 위치에서의 주유소 가격을 기준점으로 잡을 cost 변수 할당
    result = gas_station[0][0] * gas_station[0][1]  # 최소 비용 값을 담을 변수, 처음 도로 길이 * 가격 정보를 할당

    for data in gas_station[1:]:   # result함수에 주유소의 첫번째 정보값은 이미 할당했으므로 1부터 슬라이싱 조회
        if cost > data[1]:
            cost = data[1]
        result += cost * data[0]

    return result   # 최소 비용 반환

if __name__ == '__main__':
    n = int(input())  # 도시의 개수를 나타내는 정수
    lengths = list(map(int, input().split()))  # 인접한 두 도시를 연결하는 도로의 길이
    prices = list(map(int, input().split()))   # 주유소의 리터당 가격

    print(solve(lengths, prices))