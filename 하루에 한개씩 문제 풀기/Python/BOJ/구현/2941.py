# boj, 2941 : 크로아티아 알파벳, python3
# 구현, 문자열 알고리즘
def croatia(l, word):
    result = [word.count(i) for i in l if i in word]

    return len(word) - sum(result)


if __name__ == "__main__":
    croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    word = input()

    print(croatia(croatia_alpabet, word))
