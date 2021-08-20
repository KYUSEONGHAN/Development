# leetcode, easy : Pailndrome Number, python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False