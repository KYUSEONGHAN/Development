def solution(s, n):
    answer = ''
    for i in s :
        if i.isupper() :
            answer += chr(ord(i)+n) if ord(i)+n < 91  else chr(ord(i)-26+n)
        elif i.islower() :
            answer += chr(ord(i)+n) if ord(i)+n < 123  else chr(ord(i)-26+n)
        elif i == ' ' :
            answer += i
    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))