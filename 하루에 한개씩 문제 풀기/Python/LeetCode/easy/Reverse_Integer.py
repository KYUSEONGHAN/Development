# leetcode, easy : reverse integer, python3
# math
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)

        if x[0] == '-':
            x = ''.join(list(reversed(x[1:])))
            result = int('-' + x)
        else:
            result = int(''.join(list(reversed(x))))

        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0

        return int(result)