class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        ret = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return True if ret == x else False