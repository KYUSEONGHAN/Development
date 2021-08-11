# HackerRank, sWAP cASE, python3
def swap_case(s):
    result = [x.lower() if x.isupper() else x.upper() for x in s]
    return ''.join(result)


if __name__ == '__main__':
    word = str(input())

    print(swap_case(word))