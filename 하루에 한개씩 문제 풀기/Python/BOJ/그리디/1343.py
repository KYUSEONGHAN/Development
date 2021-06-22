# boj, 1343 : 폴리오미노, python3
def polyomino(l):
    result = ''

    for i in l:
        if len(i) % 2 != 0:
            return -1
        else:
            var = len(i)
            while True:
                if var < 2:
                    break
                if var >= 4:
                    result += 'AAAA'
                    var -= 4
                else:
                    result += 'BB'
                    var -= 2
        result += '.'

    return result[:-1]


board = input().split('.')

print(polyomino(board))
