# 수정 전

# boj, 1436 : 영화감독 숌, python3
import sys

N = int(sys.stdin.readline())

end = '666'

if N == 0:
    print("end")
else:
    print(str(N-1)+end)


# 수정 후
import sys

def shun(n):
    end = 666
    while n != 0:
        if '666' in str(end):
            n -= 1
        end += 1
    return end

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(shun(n) - 1)