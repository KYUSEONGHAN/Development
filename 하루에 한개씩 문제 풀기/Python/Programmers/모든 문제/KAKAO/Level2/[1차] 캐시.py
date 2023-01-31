# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# programmers, level2: 2018 kakao blind recruit, [1차] 캐시, python3
def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()

            if cache:
                if city in cache:
                    answer += 1
                    cache.remove(city)
                    cache.insert(0, city)
                else:
                    if len(cache) >= cacheSize:
                        cache.pop()
                    cache.insert(0, city)
                    answer += 5
            else:
                cache.append(city)
                answer += 5

    print(cache)
    return answer

if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 52
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25