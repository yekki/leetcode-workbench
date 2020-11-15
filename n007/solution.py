INPUT = 3210
EXPECTED = 123

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return x
        ret = int(str(x)[::-1]) if x >0 else - int(str(-x)[::-1])
        return ret if ret >= pow(-2, 31) and ret <= pow(2, 31) - 1 else 0


if __name__ == "__main__":
    print("hello")
