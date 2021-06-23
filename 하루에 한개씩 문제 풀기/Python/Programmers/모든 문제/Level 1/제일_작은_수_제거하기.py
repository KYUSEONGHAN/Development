## 시간초과 코드
def solution(arr):
    return [i for i in arr if i != min(arr)] if len(arr) > 1 else [-1]

## 정답 코드
# programmers, phase1 : 제일 작은 수 제거하기, python
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]


## 최적 코드
# - , - , - , - , jdyong 외 62 명 님 코드 참고
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
